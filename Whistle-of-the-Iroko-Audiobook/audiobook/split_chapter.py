#!/usr/bin/env python3
"""Split a story chapter into short, sentence-aligned narration chunks.

Usage: split_chapter.py CHAPTER_NUMBER [MAX_CHARS]
  CHAPTER_NUMBER: 1..10, or 'E' for the epilogue
  MAX_CHARS: target chunk size (default 450 — shorter = more pauses)

Writes parts/Chapter-NN/text-XX.txt and prints the chunks with char counts.
"""
import re, sys, os

SRC = '/home/user/The-Whistle-of-the-Iroko.md'
OUT = '/home/user/audiobook/parts'

def get_chapter(text, num):
    lines = text.splitlines()
    idx = [i for i, l in enumerate(lines) if l.startswith('## ')]
    headings = [lines[i] for i in idx]
    if num == 'E':
        pos = [i for i, h in enumerate(headings) if h.startswith('## EPILOGUE')][0]
    else:
        w = ['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN'][num-1]
        pos = [i for i, h in enumerate(headings) if h.startswith(f'## CHAPTER {w}:')][0]
    start = idx[pos] + 1
    end = idx[pos+1] if pos+1 < len(idx) else len(lines)
    return '\n'.join(lines[start:end])

def clean(t):
    t = re.sub(r'\*+', '', t)          # markdown emphasis
    t = re.sub(r'[“”]', '"', t)
    t = re.sub(r'[‘’]', "'", t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def split_sentences(t):
    # keep sentence-ish boundaries (., !, ?, and em-dash pauses)
    parts = re.split(r'(?<=[.!?…])\s+', t)
    out = []
    for p in parts:
        # further split long sentences at em-dashes for more pause points
        if len(p) > 200:
            subs = re.split(r'(?<=—)\s*', p)
            out.extend([s for s in subs if s.strip()])
        else:
            out.append(p)
    return [s.strip() for s in out if s.strip()]

def chunk(sents, maxc):
    chunks, cur = [], ''
    for s in sents:
        if len(cur) + len(s) + 1 > maxc and cur:
            chunks.append(cur)
            cur = s
        else:
            cur = (cur + ' ' + s).strip() if cur else s
    if cur:
        chunks.append(cur)
    return chunks

raw = sys.argv[1] if len(sys.argv) > 1 else '1'
num = 'E' if raw.lower() == 'e' else int(raw)
maxc = int(sys.argv[2]) if len(sys.argv) > 2 else 450

text = open(SRC).read()
body = clean(get_chapter(text, num))
sents = split_sentences(body)
chunks = chunk(sents, maxc)

n = str(num).zfill(2) if num != 'E' else 'E'
d = os.path.join(OUT, f'Chapter-{n}')
os.makedirs(d, exist_ok=True)
for i, c in enumerate(chunks, 1):
    open(os.path.join(d, f'text-{i:02d}.txt'), 'w').write(c)
    print(f'=== CHUNK {i:02d} ({len(c)} chars) ===')
    print(c)
    print()
print(f'TOTAL: {len(chunks)} chunks for chapter {num}')

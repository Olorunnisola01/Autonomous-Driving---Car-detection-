#!/usr/bin/env python3
"""Assemble ordered audio clips into one normalized MP3 with pauses and optional slowdown.

Usage: assemble.py OUTPUT.mp3 GAP_SECONDS [--tempo 0.70] FILE1.mp3 FILE2.mp3 ...
"""
import subprocess, sys, os

ff = open(os.path.expanduser('/home/user/.ffmpeg_path')).read().strip()
args = sys.argv[1:]
out = args[0]
gap = float(args[1])
tempo = 1.0
rest = args[2:]
if rest and rest[0] == '--tempo':
    tempo = float(rest[1])
    rest = rest[2:]
files = rest

sil = '/tmp/whistle_silence.mp3'
subprocess.run(
    [ff, '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono',
     '-t', str(gap), '-q:a', '9', sil],
    check=True, capture_output=True)

ordered = []
for f in files:
    if ordered:
        ordered.append(sil)
    ordered.append(f)

cmd = [ff, '-y']
for f in ordered:
    cmd += ['-i', f]
n = len(ordered)
chain = []
for i in range(n):
    c = f'[{i}:a]aresample=44100'
    if tempo != 1.0:
        c += f',atempo={tempo}'
    c += f',aformat=channel_layouts=mono[a{i}]'
    chain.append(c)
chain.append(''.join(f'[a{i}]' for i in range(n)) +
             f'concat=n={n}:v=0:a=1,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100[aout]')
cmd += ['-filter_complex', ';'.join(chain), '-map', '[aout]',
        '-c:a', 'libmp3lame', '-q:a', '2', out]
subprocess.run(cmd, check=True, capture_output=True)
print('assembled ->', out)

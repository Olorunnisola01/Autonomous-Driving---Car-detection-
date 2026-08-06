#!/usr/bin/env python3
"""Animate S01_Step01 (candlelit bindery) into a video with candlelight flicker
and drifting dust motes — no Ken Burns zoom."""

import numpy as np
from PIL import Image
import imageio.v2 as iio
import random
import os

# Load source image
img_path = '/home/user/Autonomous-Driving---Car-detection-/the_dukes_obsession/images/act1/S01_Step01_candlelit_bindery.png'
src = np.array(Image.open(img_path).convert('RGB'))
H, W, _ = src.shape
# Ensure even dimensions for H.264
W = W - (W % 2)
H = H - (H % 2)
src = src[:H, :W, :]
print(f"Source image: {W}x{H}")

# Animation parameters
FPS = 24
DURATION = 10  # seconds
TOTAL_FRAMES = FPS * DURATION

# Generate dust particles
random.seed(42)
NUM_PARTICLES = 60

class Particle:
    def __init__(self, respawn=True):
        self.respawn = respawn
        self.reset(full=True)
    
    def reset(self, full=False):
        self.x = random.uniform(0, W)
        self.y = random.uniform(0, H) if full else random.uniform(H * 0.3, H)
        self.size = random.uniform(1.0, 3.5)
        self.alpha = random.uniform(0.15, 0.55)
        self.vx = random.uniform(-0.3, 0.3)
        self.vy = random.uniform(-0.5, -0.1)  # upward drift
        self.life = random.uniform(0.7, 1.0)
        self.phase = random.uniform(0, 2 * np.pi)
    
    def update(self, t):
        self.x += self.vx + 0.1 * np.sin(t * 2 + self.phase)
        self.y += self.vy
        self.life -= 0.002
        if self.life <= 0 or self.y < -10 or self.x < -10 or self.x > W + 10:
            if self.respawn:
                self.reset(full=False)
            else:
                self.life = 0

particles = [Particle() for _ in range(NUM_PARTICLES)]

# Pre-compute flicker LUT (per-frame brightness multiplier)
flicker_lut = []
for f in range(TOTAL_FRAMES):
    t = f / FPS
    # Combine multiple sine waves for organic flicker
    v = (
        1.0
        + 0.025 * np.sin(2 * np.pi * 1.3 * t + 0.5)
        + 0.015 * np.sin(2 * np.pi * 2.7 * t + 1.3)
        + 0.010 * np.sin(2 * np.pi * 5.1 * t + 2.1)
        + 0.005 * np.sin(2 * np.pi * 11.3 * t)
        + random.gauss(0, 0.008)
    )
    flicker_lut.append(v)

# Color warmth pulse
warmth_lut = []
for f in range(TOTAL_FRAMES):
    t = f / FPS
    w = 1.0 + 0.015 * np.sin(2 * np.pi * 0.8 * t)
    warmth_lut.append(w)

def draw_particle(frame, p):
    """Draw a soft glow particle."""
    if p.life <= 0:
        return
    cx, cy = int(p.x), int(p.y)
    r = int(p.size * 2.5)
    x0, y0 = max(0, cx - r), max(0, cy - r)
    x1, y1 = min(W, cx + r + 1), min(H, cy + r + 1)
    if x1 <= x0 or y1 <= y0:
        return
    alpha = p.alpha * p.life
    for y in range(y0, y1):
        for x in range(x0, x1):
            dx = (x - cx) / r
            dy = (y - cy) / r
            d = np.sqrt(dx * dx + dy * dy)
            if d > 1.0:
                continue
            # Soft glow falloff
            falloff = (1.0 - d * d) ** 1.5
            a = alpha * falloff
            # Warm white particle
            frame[y, x, 0] = min(255, int(frame[y, x, 0]) + int(255 * a))
            frame[y, x, 1] = min(255, int(frame[y, x, 1]) + int(240 * a))
            frame[y, x, 2] = min(255, int(frame[y, x, 2]) + int(200 * a))

def apply_flicker(frame, brightness, warmth):
    """Apply candlelight flicker and warmth shift."""
    # Convert to float
    f = frame.astype(np.float32)
    # Apply brightness
    f *= brightness
    # Apply warmth: boost red channel slightly, reduce blue slightly
    f[..., 0] *= warmth
    f[..., 2] /= warmth
    # Clamp
    np.clip(f, 0, 255, out=f)
    return f.astype(np.uint8)

# Generate frames
output_dir = '/home/user/Autonomous-Driving---Car-detection-/the_dukes_obsession'
output_path = os.path.join(output_dir, 'S01_Step01_animated.mp4')
print(f"Writing video to {output_path}")
print(f"Total frames: {TOTAL_FRAMES}, FPS: {FPS}")

writer = iio.get_writer(output_path, fps=FPS, codec='libx264',
                        macro_block_size=1, quality=9)

for f_idx in range(TOTAL_FRAMES):
    t = f_idx / FPS
    # Start from source
    frame = src.copy()
    
    # Apply flicker + warmth
    brightness = flicker_lut[f_idx]
    warmth = warmth_lut[f_idx]
    frame = apply_flicker(frame, brightness, warmth)
    
    # Draw particles
    for p in particles:
        draw_particle(frame, p)
        p.update(t)
    
    writer.append_data(frame)
    
    if f_idx % 24 == 0:
        print(f"  Frame {f_idx}/{TOTAL_FRAMES} ({100*f_idx/TOTAL_FRAMES:.0f}%)")

writer.close()
print(f"\nDone! Video saved to {output_path}")

# Verify
import os
size_mb = os.path.getsize(output_path) / (1024 * 1024)
print(f"Video size: {size_mb:.2f} MB")
print(f"Duration: {DURATION}s at {FPS}fps")
print(f"Resolution: {W}x{H}")

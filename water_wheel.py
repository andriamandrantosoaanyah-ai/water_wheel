# MyMaharat
# Water Breathing, water whe...

import pygame, math, random

pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
W, H = win.get_size()
fade = pygame.Surface((W, H))
fade.fill((0, 10, 30))
fade.set_alpha(30)
draw, drops, t = pygame.draw, [], 0
cx, cy = W / 2, H/2
R = min(W,H) * 0.27 #the wheel fits any screen

while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            raise SystemExit
    t += 0.05
    win.blit(fade, (0, 0))
    a = t *3 # the wheel turns
    x = cx +math.cos(a) * R
    y = cy + math.sin(a)* R
    for i in range(16):
        drops.append([x, y, random.uniform(-3, 3), random.uniform(-3, 3), 20])

    for d in drops:
        d[0] += d[2]
        d[1] += d[3]+0.8 #water falls
        d[4] -= 0.3
        blue = (40, 120+int(d[4]*6), 255)
        draw.circle(win, blue, d[:2], max(1, d[4]))
    drops = [d for d in drops if d[4] > 1]
    tip = (cx + math.cos(a) * R*1.35, 
           cy + math.sin(a) * R*1.35)
    draw.line(win, "silver", (x, y), tip, 12)
    draw.circle(win, "white", (x, y), 14)
    pygame.display.flip()
    pygame.time.wait(30)
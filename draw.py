from display import *
import math


def draw_line( x0, y0, x1, y1, screen, color ):
    # check going from left to right and from down to up    
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    if x1 == x0:
        if y0 > y1:
            y0, y1 = y1, y0
    # identify slope
    try:
        m = (float(y1) - y0) / (x1 - x0)
    except: m = 100

    # for slope 0 <= m <= 1
    # octant 1
    if (m <= 1 and m >= 0):
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2*A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2*B
            x += 1
            d += 2*A

    # for slope >= 1
    # octant 2
    if (m > 1):
        
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A + 2*B
        while (y <= y1):
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2*A
            y += 1
            d += 2*B


    # for slope -1 <= m < 0
    # octant 8
    if (-1 <= m < 0):        
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2*A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2*B
            x += 1
            d += 2*A

    # for slope m < -1
    # octant 7
    if (m < -1):
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A - 2*B
        while (y >= y1):
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2*A
            y -= 1
            d -= 2*B
        
    return screen


s = new_screen()

for i in range(0, 499, 2):
    draw_line(i, 0, 499, 499-i, s, [0, 0, int((i/2) %255)])
for i in range(0, 499, 2):
    draw_line(0, i, 499-i, 499, s, [int((i/2.5) %255), 0, 0])



for x in range(0, 499, 2):
    for y in range(0, 499, 2):
        d = int(math.sqrt( (250-x)**2 + (250 - y)**2))
        if d == 200:
            if x% 3 == 1:
                color = [0, 0, 200]
            else: color = [200, 0, 0]
            draw_line(250, 250, x, y, s, color)

fname = "image.ppm"

save_ppm(s, fname)
print(fname)

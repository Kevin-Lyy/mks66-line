from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    if x0 > x1:
        draw_line(x1,y1,x0,y0,screen, color)
        return

    x = x0
    y = y0
    A = y1 - y0
    B = -1 *(x1 - x0)

    # Octant 1
    if 0 <= A and A <= -B:
        d = B + 2 * A
        while x <= x1:
            plot(screen,color,x,y)
            if d >= 0:
                y += 1
                d += B * 2
            x += 1
            d += A * 2

    # Octant 2
    elif 0 <= A and -B <= A:
        d = A + 2 * B
        while y <= y1:
            plot(screen,color,x,y)
            if d <= 0:
                x += 1
                d += A * 2
            y += 1
            d += B * 2

    # Octant 7
    elif A <= 0 and A <= B:
        d = A + -2 * B
        while y1 <= y:
            plot(screen,color,x,y)
            if d >= 0:
                x += 1
                d += A * 2
            y += -1
            d += -2 * B

    # Octant 8
    elif A <= 0 and B <= A:
        d = 2 * A + -B
        while x1 >= x:
            plot(screen,color,x,y)
            if d <= 0:
                y += -1
                d += -2 * B
            x += 1
            d += A * 2
    else:
        return

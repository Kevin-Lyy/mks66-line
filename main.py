from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

draw_line( 250, 250, 500, 500, screen, color )
draw_line( 250, 250, 500, 350, screen, color )
draw_line( 250, 250, 500,  50, screen, color )
draw_line( 250, 250, 500, 150, screen, color )
draw_line( 250, 250, 350,   0, screen, color )
draw_line( 250, 250, 250,   0, screen, color )
draw_line( 250, 250, 350, 500, screen, color )
draw_line( 250, 250, 250, 500, screen, color )
draw_line( 250, 250, 500, 250, screen, color )

draw_line( 250, 250,   0,   0, screen, color )
draw_line( 250, 250,   0, 150, screen, color )
draw_line( 250, 250, 150,   0, screen, color )
draw_line( 250, 250,   0, 500, screen, color )
draw_line( 250, 250,   0, 350, screen, color )
draw_line( 250, 250, 150, 500, screen, color )
draw_line( 250, 250, 250, 500, screen, color )
draw_line( 250, 250,   0, 250, screen, color )
draw_line( 250, 250, 250,   0, screen, color )

#-------------------------------------------------------
#top lines
# draw_line(50,400,250,430,screen,[0,150,255])
# draw_line(255,432,450,460,screen,[0,150,255])
#
# #bottom lines
# draw_line(50,100,250,70,screen,[0,150,255])
# draw_line(255,68,450,38,screen,[0,150,255])
#
# #vertical lines
# #leftmost
# draw_line(50,400,50,255,screen,[0,150,255])
# draw_line(50,100,50,245,screen,[0,150,255])
# #left-middle
# draw_line(250,430,250,255,screen,[0,150,255])
# draw_line(250,245,250,70,screen,[0,150,255])
# #right-middle
# draw_line(255,432,255,255,screen,[0,150,255])
# draw_line(255,245,255,68,screen,[0,150,255])
# #rightmost
# draw_line(450,460,450,255,screen,[0,150,255])
# draw_line(450,245,450,38,screen,[0,150,255])
#
# #horizontal lines
# draw_line(50,255,250,255,screen,[0,150,255])
# draw_line(50,245,250,245,screen,[0,150,255])
#
# draw_line(255,255,450,255,screen,[0,150,255])
# draw_line(255,245,450,245,screen,[0,150,255])

display(screen)
save_extension(screen, 'img.png')

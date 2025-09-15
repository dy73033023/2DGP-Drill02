from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character= load_image('character.png')

def rectangle_move():
    x = 400
    y = 90
    while (x < 780):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x,y)
         x+=10
         delay(0.01)

    while (y < 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        y+=10
        delay(0.01)

    while (x > 20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        x-=10
        delay(0.01)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        y-=10
        delay(0.01)

    while (x < 400):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x,y)
         x+=10
         delay(0.01)


def circle_move():
    cx, cy = 400, 330
    r = 200
    for degree in range(270, 270+360, 5):
        theta = math.radians(degree)
        x = cx + r * math.cos(theta)
        y = cy - r * math.sin(theta)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

while(1):
    rectangle_move()
    circle_move()

close_canvas()







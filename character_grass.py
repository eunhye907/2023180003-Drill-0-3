from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
	clear_canvas_now()
	boy.draw_now(x,y)
	delay(0.1)

def run_circle():
	print('CIRCLE')

	r, cx, cy = 300, 800//2, 600//2

	for degree in range(0, 360, 3):

		theta = math.radians(degree)
		x = r* math.cos(theta) + cx
		y = r* math.sin(theta) + cy
		draw_boy(x,y)
		

def run_top():
	print('TOP')
	for x in range(0, 800, 10):
		draw_boy(x, 550)

	pass

def run_right():
	print('RIGHT')
	for y in range(550, 0, -10):
		draw_boy(790, y)

	pass

def run_bottom():
	print('BOTTOM')
	for x in range(800, 0, -10):
		draw_boy(x, 10)

	pass

def run_left():
	print('LEFT')
	for y in range(0, 550, 10):
		draw_boy(10, y)
	pass

def run_rectangle():
	print('RECTANGLE')

	run_top()
	run_right()
	run_bottom()
	run_left()

	pass

def run_straight():
	for x in range(0, 800, 10):
		draw_boy(x, 10)
	pass

def run_back():
	y = 0
	for x in range(800, 400, -10):
		y = y + 10
		draw_boy(x,y)
	pass
		
def run_front():
	y = 400
	for x in range(400, 0, -10):
		y = y - 10
		draw_boy(x,y)
	pass

def run_triangle():
	print('TRIANGLE')
	run_straight()
	run_back()
	run_front()

	pass
	
while True:
	# run_circle()
	# run_rectangle()
	run_triangle()
	break


close_canvas()

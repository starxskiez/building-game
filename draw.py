import turtle
from move import cursor

# Draw Turtle
draw_turtle = turtle.Turtle()
color = "black"
draw_turtle.fillcolor(color)

draw_turtle.hideturtle()
draw_turtle.penup()
draw_turtle.speed(0)

# Colors
def pink():
  global color
  color = "pink"
def firebrick():
  global color
  color = "darkred"
def orange():
  global color
  color = "orange"
def gold():
  global color
  color = "gold"
def forestgreen():
  global color
  color = "forestgreen"
def steelblue():
  global color
  color = "steelblue"
def darkslateblue():
  global color
  color = "darkslateblue"
def brown():
  global color
  color = "brown"
def black():
  global color
  color = "black"
def white():
  global color
  color = "white"


isDrawing = False
# Draws Brick
def drawing():
  global isDrawing
  if isDrawing:
    return
  isDrawing = True
  draw_turtle.fillcolor(color)
  draw_turtle.goto(cursor.pos()) 
  draw_turtle.forward(5)
  draw_turtle.left(90)
  draw_turtle.forward(5)
  draw_turtle.left(90)
  draw_turtle.pendown()
  draw_turtle.begin_fill()
  
  for d in range(4):
    draw_turtle.forward(10)
    draw_turtle.left(90)
  draw_turtle.end_fill()
  draw_turtle.penup()
  draw_turtle.forward(5)
  draw_turtle.left(90)
  draw_turtle.forward(5)
  draw_turtle.left(90)
  isDrawing = False
  

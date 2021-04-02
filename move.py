import turtle

# Cursor Turtle
cursor = turtle.Turtle()
cursor.shape("square")
cursor.color('grey')
cursor.shapesize(0.5)
cursor.speed(0)
cursor.penup()
cursor.fillcolor("black")
cursor.goto(5, 5)

# Key Press Functions
def right():
  cursor.forward(10)
def left():
  cursor.backward(10)
def up():
  cursor.sety(cursor.ycor()+10)
def down():
  cursor.sety(cursor.ycor()-10)

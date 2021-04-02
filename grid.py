import turtle



# Grid Turtle
grid_turtle = turtle.Turtle()
grid_turtle.speed(0)
grid_turtle.hideturtle()
grid_turtle.pensize(.2)
gc = "black"
grid_turtle.color(gc) #can let players choose grid color

# Grid
def grid():
  grid_turtle.penup()
  grid_turtle.goto(-150, 150)
  grid_turtle.pendown()

  for g in range(15):
    grid_turtle.forward(300)
    grid_turtle.right(90)
    grid_turtle.forward(10)
    grid_turtle.right(90)
    
    grid_turtle.forward(300)
    grid_turtle.left(90)
    grid_turtle.forward(10)
    grid_turtle.left(90)
  
  grid_turtle.left(90) 
  
  for g in range(15):
    grid_turtle.forward(300)
    grid_turtle.right(90)
    grid_turtle.forward(10)
    grid_turtle.right(90)
    
    grid_turtle.forward(300)
    grid_turtle.left(90)
    grid_turtle.forward(10)
    grid_turtle.left(90)
  grid_turtle.forward(300)
  grid_turtle.backward(300)
  grid_turtle.left(90)
  grid_turtle.forward(300)



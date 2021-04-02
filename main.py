# Adding Console Commands
# Fixing Bugs


import turtle, os, time

import grid, move, draw, console
from draw import cursor
from grid import grid_turtle, gc

# Setup
os.system("clear")

# Main Screen
scr = turtle.Screen()
scr.title("Building Game")
scr.setup(width = 800, height = 800)
print("Welcome to The Building Game...")
time.sleep(2)
print("An M & L project...")
time.sleep(2)
print("We present to you...")
grid.grid()
bg = "white"
turtle.bgcolor(bg) #lightblue later, maybe we can l


#Help turtle
help_turtle = turtle.Turtle()
help_turtle.hideturtle()
help_turtle.penup()
help_turtle.goto(-320, -70) #-300, 100
help_turtle.write('Colors: \n 0. White (Eraser)\n 1. Pink\n 2. Firebrick (Red)\n 3. Orange\n 4. Gold (Yellow)\n 5. Forest Green (Green)\n 6. Steel Blue (Blue)\n 7. Dark Slate Blue (Purple)\n 8. Brown\n 9. Black\n ')
help_turtle.goto(0, 200) #-300, 270
help_turtle.write("Press the arrow keys or wasd to move the black square or cursor on the screen. \nTo change the color you want to draw with, press numbers 0-9 on your keyboard.\nYou can look at the color list to see all the colors and their corresponding number.\nFinally, if you want to place a block or a brick, press space.\nYour brick should appear as the color you chose.", font=("Verdana", 8, "normal"), align = "center")


os.system("clear")
console.main()
#print("")
#input("If you want to suggest more colors we can use, type them here. Here is the list of colors: https://matplotlib.org/stable/gallery/color/named_colors.html\n> ")


# Key Press  
# Colors
scr.onkeypress(draw.pink,'1')
scr.onkeypress(draw.firebrick,'2')
scr.onkeypress(draw.orange,'3') 
scr.onkeypress(draw.gold,'4')
scr.onkeypress(draw.forestgreen,'5')
scr.onkeypress(draw.steelblue,'6') 
scr.onkeypress(draw.darkslateblue,'7') 
scr.onkeypress(draw.brown,'8') 
scr.onkeypress(draw.black,'9')
scr.onkeypress(draw.white,'0')


# Draw
scr.onkeypress(draw.drawing,'space')

# Arrow Keys
scr.onkeypress(move.up,'Up') 
scr.onkeypress(move.left,'Left') 
scr.onkeypress(move.down,'Down')
scr.onkeypress(move.right,'Right') 

# WASD
scr.onkeypress(move.up,'w') 
scr.onkeypress(move.left,'a') 
scr.onkeypress(move.down,'s') 
scr.onkeypress(move.right,'d')


# Mainloop
while True:
  grid_turtle.color(gc)
  # Boundaries
  if (cursor.xcor() <= -149):
    cursor.goto(-145, cursor.ycor())

  if (cursor.xcor() >= 149):
    cursor.goto(145, cursor.ycor())

  if (cursor.ycor() >= 149):
    cursor.goto(cursor.xcor(), 145)

  if (cursor.ycor() <= -149):
    cursor.goto(cursor.xcor(), -145)
  

  # Listening for Key Press
  scr.listen()

  # Updates the screen
  scr.update()
  
scr.mainloop()
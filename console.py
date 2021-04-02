import os, time
from grid import gc

# Colors
teal = '\033[96m'
reset = '\033[0m'
bold = '\033[1m'
black  = '\33[30m'
red    = '\33[31m'
green  = '\33[32m'
orange = '\33[33m'
blue   = '\33[34m'
violet = '\33[35m'
cyan  = '\33[36m'
pink= '\033[95m'
yellow = '\033[93m'
blue   = '\033[34m'
white  = '\33[37m'

# Main Function for the Console
def main():
  os.system("clear")
  print(bold + cyan + "The Building Game: An M & L project...\n" + reset)
  howto()
  cmd()

# How to Play Function
def howto():
  print(bold + cyan + "How To Play:\n")
  print(bold + cyan + "Press the arrow keys or wasd to move the black square or cursor on the screen. To change the color you want to draw with, press numbers 0-9 on your keyboard. You can look at the color list to see all the colors and their corresponding number. Finally, if you want to place a block or a brick, press space. Your brick should appear as the color you chose." + reset)
  print(bold + "\nColors:\n" + reset + "0. White (Eraser)\n" + pink + "1. Pink\n" + red + "2. Firebrick (Red)\n" + orange + "3. Orange\n" + yellow + "4. Gold (Yellow)\n" + green + "5. Forest Green (Green)\n" + blue + "6. Steel Blue (Blue)\n" + violet + "7. Dark Slate Blue (Purple)\n" + red + "8. Brown\n" + white + "9. Black\n" + reset)

# Commands
def cmd():
  print("Commands (type cmdlist for a full list of commands and dont use yet its broken):")
  cmd = input("> ")
  if cmd == "cmdlist":
    cmdlist()
  elif cmd == "gc":
    gc()
  else:
    print

# cmdlist command
def cmdlist():
  os.system("clear")
  print(bold + "Commands:" + reset)
  print("1. cmdlist - Returns full list of commands. Gets updated frequently.")
  print("2. gc - Allows you to change the color of the grid.")
  print()
  cmd = input("Commands:\n[1] back\n> ")
  if cmd == "back" or cmd == "1":
    main()

def gc():
  global gc
  while True:
    os.system("clear")
    color = input("What color would you like the grid to be (adding more options)?\n1. white\n2. black\n3. light blue\n4. back\n> ")
    if color == "white" or color == "1":
      gc = "white"
      break
    elif color == "black" or color == "2":
      gc = "black"
      break
    elif color == "light blue" or color == "3":
      gc = "lightblue"
      break
    elif color == "back":
      main()
    else:
      print(red + "Invalid Option. " + reset)
      yn = input(green + "Do you want to go back (y/n)? ")
      
      if yn == "y":
        main()
        break
      else:
        pass



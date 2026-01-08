# Day 3 – Treasure Island
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Writing multi-line strings using triple quotes
# - Displaying ASCII art in the console
# - Using conditional logic (if / elif / else)
# - Nesting conditionals to create decision trees
# - Comparing user input to expected values
# - Using .lower() to normalize user input
#
# This project represents my first text-based game
# and my introduction to program flow and branching logic.

print(r'''   __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}''')

# Introduction to the game
print("Welcome to Treasure Island.\nYour Mission is to find the Treasure.")

# First decision point: left or right
road = input(
    "You are at a cross road. Where do you want to go? Type 'left' or 'right'\n "
).lower()

if road == "left":

    # Second decision point: wait or swim
    lake = input(
        "You've come to a lake. There is an island in the middle of lake.\n"
        "Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
    ).lower()

    if lake == "wait":

        # Third decision point: choose a door
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\n"
            "One red, one yellow and one blue. Which color do you choose?\n"
        ).lower()

        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "yellow":
            print("You win!")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over")

    else:
        print("Attacked by trout. Game Over.")

else:
    print("Fall into a hole. Game Over")

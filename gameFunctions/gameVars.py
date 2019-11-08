from random import randint

# 'basket' of choices
choices=["rock","paper","scissors"]

# adding lives --> when one of the other gets to 0, win / lose
player_lives = 5
computer_lives = 5

total_lives= 5

# let the ai make a choice
computer=choices[randint(0,2)]

# setup a game loop here so we dont have to keep restarting
player = False

#decrotive line
line = "============================================"
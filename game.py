from random import randint

choices=["rock","paper","scissors"]

# let the ai make a choice
computer=choices[randint(0,2)]

# setup a game loop here so we dont have to keep restarting
player = False

while player is False:
	player=input("choose rock, paper, or scissors")

	#start doing some logic and condition checking
	print("computer: ", computer, "player: ", player)

	#always check a breaking condition first
	if player == computer:
		# we have a tie, no point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print ("you chose to quit, quitter.")
		exit()

	else:
		print("NOT a tie. Now we can check other conditions")
		if player == "rock":
			print("check and see what the computer is, and win or lose")

	player = False
	computer=choices[randint(0,2)]
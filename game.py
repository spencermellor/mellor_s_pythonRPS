from random import randint
from gameFunctions import winlose, gameVars

while gameVars.player is False:
	print("====================================\n")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("====================================\n")
	print("Choose your weapon!\n")
	player=input("choose rock, paper, or scissors: \n")

	#start doing some logic and condition checking
	print("computer: ", gameVars.computer, "player: ", gameVars.player)

	#always check a breaking condition first
	if player == gameVars.computer:
		# we have a tie, no point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print ("you chose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "slices", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1


	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "slices", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	if gameVars.computer_lives is 0:
		winlose.winorlose("won")
		
	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]





from gameFunctions import gameVars

# Defined the function
def compare (player):
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
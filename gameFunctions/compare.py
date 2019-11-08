from gameFunctions import gameVars

# Defined the function
def compare (player):
	#always check a breaking condition first
		if player == gameVars.computer:
			# we have a tie, no point in going any further
			print("Tie, no one wins! try again!")
			print(gameVars.line)

		elif player == "quit":
			print ("you chose to quit, quitter.")
			print(gameVars.line)
			exit()

		elif player == "rock":
			if gameVars.computer == "paper":
				print("You lose!", gameVars.computer, "covers", player)
				print(gameVars.line)
				gameVars.player_lives = gameVars.player_lives - 1
			else:
				print("You won!", player, "smashes", gameVars.computer)
				print(gameVars.line)
				gameVars.computer_lives = gameVars.computer_lives -1

		elif player == "paper":
			if gameVars.computer == "scissors":
				print("You lose!", gameVars.computer, "slices", player)
				print(gameVars.line)
				gameVars.player_lives = gameVars.player_lives -1
			else:
				print("You won!", player, "covers", gameVars.computer)
				print(gameVars.line)
				gameVars.computer_lives = gameVars.computer_lives -1


		elif player == "scissors":
			if gameVars.computer == "rock":
				print("You lose!", gameVars.computer, "smashes", player)
				print(gameVars.line)
				gameVars.player_lives = gameVars.player_lives -1
			else:
				print("You won!", player, "slices", gameVars.computer)
				print(gameVars.line)
				gameVars.computer_lives = gameVars.computer_lives -1
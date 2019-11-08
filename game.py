from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("====================================\n")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("====================================\n")
	print("Choose your weapon!\n")
	player=input("choose rock, paper, or scissors: \n")

	#start doing some logic and condition checking
	print("computer: ", gameVars.computer, "player: ", gameVars.player)
	
	# check the function

	compare.compare (player)

	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	if gameVars.computer_lives is 0:
		winlose.winorlose("won")
		
	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]





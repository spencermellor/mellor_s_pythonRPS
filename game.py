from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print(gameVars.line)
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print(gameVars.line)
	print("Choose your weapon!")
	print(gameVars.line)
	player=input("Choose rock, paper, or scissors: \n")
	print(gameVars.line)

	#start doing some logic and condition checking
	print("Computer chose: ", gameVars.computer, "--------- YOU chose: ", gameVars.player)
	
	# check the function

	compare.compare (player)

	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	if gameVars.computer_lives is 0:
		winlose.winorlose("won")
		
	else:
		player = False
		gameVars.computer = gameVars.choices[randint(0,2)]





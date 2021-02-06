from src.services.game import Game

game = Game()

num_of_players = 2
for i in range(num_of_players):
    name = input("Enter player's name:")
    game.add_player(name)

game.add_board(100)
game.add_dice(6)

snakes_and_ladders = {
	(99, 10), (8, 35), (40, 22), (91, 45), (46, 83),
	(88, 32), (66, 94), (54, 86), (44, 3), (74, 62),
	(1, 9), (8, 4), (2, 11), (12, 3)	
}
for item in snakes_and_ladders:
	game.add_side_effect(*item)
game.play()

from time import sleep

from .player import Player
from .dice import Dice
from .board import Board
from .side_effect import SideEffect


class Game:
    players: list = []
    dice: Dice = None
    board: Board = None
    victory: int = 100

    def play(self):

        while True:
            for player in self.players:
                sleep(2)
                num = self.dice.roll()

                print('{} got {}'.format(player.name, num))

                player.advance(num)

                side_effect = self.board.check_side_effect(player.place)
                if side_effect:
                    print("Player {} ENCOUNTERED {}".format(player.name, side_effect.name))
                    player.move(side_effect.dest)

                print('{} moved to {}'.format(player.name, player.place))
                if self._check_win(player):
                    print("Player {} wins!".format(player.name))
                    return

    def _check_win(self, player: Player):
        return player.place >= self.victory

    def add_player(self, name: str):
        player = Player(name)
        self.players.append(player)

    def add_dice(self, faces: int):
        self.dice = Dice(faces)

    def add_board(self, size: int):
        self.board = Board(size)

    def add_side_effect(self, source, dest):
        name = 'snake' if source > dest else 'ladder'
        self.board.add_side_effect(SideEffect(source, dest, name))

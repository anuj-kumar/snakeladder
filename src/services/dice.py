from random import randint


class Dice:
    def __init__(self, num_of_faces: int):
        self.num_of_faces = num_of_faces

    def roll(self):
        return randint(1, self.num_of_faces)


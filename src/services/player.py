class Player:
    place = 0
    name = ''

    def __init__(self, name):
        self.name = name

    def advance(self, num: int):
        """
        :param:
        num -> number of places to advance
        :return:
        """
        self.move(self.place + num)


    def move(self, place: int):
        self.place = place


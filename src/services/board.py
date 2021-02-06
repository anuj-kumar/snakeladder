from src.services.side_effect import SideEffect


class Board:

    side_effects = {}
    size = 100

    def __init__(self, size):
        self.size = size

    def add_side_effect(self, side_effect: SideEffect):
        self.side_effects[side_effect.source] = side_effect

    def check_side_effect(self, place: int) -> SideEffect:
        if place in self.side_effects:
            return self.side_effects.get(place)
        return None

from config import HOUSE_ROOMS
import random

class Environment:
    def __init__(self):
        self.rooms = HOUSE_ROOMS

    def get_random_room(self):
        return random.choice(self.rooms)

from enum import Enum

class GameMode(Enum):
    WaitingToStart = 1
    AboutToPlay = 2
    Playing = 3
    Finished = 4
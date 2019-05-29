import random
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
    def getMove(self, grid):
    	# Selects a random move and returns it
    	moveset = grid.getAvailableMoves()
    	return random.choice(moveset)[0] if moveset else None
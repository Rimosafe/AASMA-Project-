from Game import Game
from Ship import Ship
from Board import Board
from Agent import RandomAgent

b1 = Board()
b1.build_fleet_random()
print(b1)

ag = RandomAgent()
ag.policy(b1)
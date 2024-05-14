from Player import Player
from Game import Game
from IA import initializer

player = Player("Player", 0)
dealer = Player("Delaer", 0)

game = Game(player=player, dealer=dealer, round=2)

initializer()

game.play()


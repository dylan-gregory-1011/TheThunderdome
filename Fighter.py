#!/usr/bin/env python
"""
Defines The Class for the fighter to be used in the battle royale game.  The attack method
is based on the different attacking methods available to the fighter.  A randomized effectiveness
is chosen based on the option chosen by the user

Option 1: Low variability, low effectiveness attack: Chooses a random effectiveness between 18 and
25
Option 2: High variability, high effectiveness attack: Chooses a random effectiveness between 10 and 35,
higher risk, higher reward attack
Option 3: Heals between 15 and 20% of the damage

"""

from random import randint

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

class Fighter(object):
    #properties
    health = 100

    def __init__(self, name, attacks):
        self.name = name
        self.fighting_moves = attacks
        print("\nFighter:: %s" % self.name)
        self.showFighterMoves()

    def showFighterMoves(self):
        """
        Print's the possible moves for the user
        """
        print("Possible moves are:\n"
              "Low Damage: %s\n"
              "High Damage: %s\n"
              "Heal: %s" % (self.fighting_moves[0], self.fighting_moves[1], self.fighting_moves[2]))

    def useMove(self, move_ix):
        """
        Calculates the proper health response from an attack that the user makes
        """
        if move_ix == 2:
            self.health += (min([randint(15,20), 100 - self.health]))
            print('\n%s choses to %s' % (self.name, self.fighting_moves[move_ix]))
            return 0
        else:
            damage = randint(18 - 8*move_ix, 25 + 10 * move_ix )
            print('\n%s choses to use %s with affect %i' % (self.name,self.fighting_moves[move_ix], abs(damage)))
            return damage

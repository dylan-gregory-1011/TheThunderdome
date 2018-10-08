#!/usr/bin/env python
"""
Defines The Class for the Thunderdome game to be used.  Allows for the user to re-initialize the
game when they want to start a new game.  The function battleRoyale drives the game between
a user and a CPU until one fighter has lost all it's health
"""

from Fighter import Fighter
from random import randint, choice
import time
import os

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

#Global variables
delay_time = 1.5

class TheThunderdome(object):
    #constants
    fighters = { #Fighting Style: [Low Attack, High Attack, Heal]
                    'Chuck Norris': ['Karate Chop', 'Drop Kick', 'Meditation'],
                    'Ron Weasley': ['Expelliarmus', 'Crucio', 'Magic Potion'],
                    '8th Grader': ['Sarcasm', 'Dab', 'Snap-chatting'],
                    'Betty White': ['Denture Throw', 'WheelChair Rush', 'Napping'],
                    'Mad Max': ['Rusty Shovel', 'Hammer', 'Nuclear Water'],
                    'Deadpool': ['Double Chop', 'Slice', 'Relax']}
    user_turn = False

    #initialization
    def __init__(self):
        self.user_fighter = self.chooseUserFighter()
        time.sleep(delay_time)
        self.fighters.pop(self.user_fighter.name)
        computer_fighter = choice(list(self.fighters))
        print("\nYou opponent will be: %s" % computer_fighter)
        self.computer_fighter = Fighter(computer_fighter, self.fighters[computer_fighter])
        input("\n\nWhen You're ready to enter the Thunderdome, press enter!")

    #methods
    def chooseUserFighter(self):
        """
        Allows the user to choose a fighter from the specified fighters

        return: A fighter based on the selection that the user has chosen.
        """
        print("Good Afternoon Thunderdome Contestant.\n\n"
              "Its a wonderful day for a battle\n\n"
              "Which Fighter would you like to choose?\n")

        for fighter in self.fighters.keys():
            print("->%s" % fighter)

        while True:
            user_name = input("Select Your Fighter: ")
            if user_name in self.fighters.keys():
                return Fighter(user_name, self.fighters[user_name])
            else:
                print("\nThe character you typed doesn't exist.  Please Try Again!")

    def battleRoyale(self):
        """
        The driving function behind the game.  This allows for the first attacker to be randomized
        and then the attack sequence to continue until someone wins.
        """
        os.system('cls'); time.sleep(delay_time)

        if randint(1,2) == 1:
            self.user_turn = True
            print("%s goes first" % self.user_fighter.name)

        else:
            print("%s goes first" % self.computer_fighter.name)

        while self.user_fighter.health >= 0 and self.computer_fighter.health >= 0:
            time.sleep(delay_time); os.system('cls')

            print("%s health: %i || %s health: %i" % (self.user_fighter.name,
                                                    self.user_fighter.health,
                                                    self.computer_fighter.name,
                                                    self.computer_fighter.health))

            self.attackOccurs()
            time.sleep(delay_time)

        if self.computer_fighter.health <= 0:
            print("Congrats, You Won!!!!")
        else:
            print("You Suck")
        return input("Continue Playing? (Y/N): ")

    def attackOccurs(self):
        """
        Ensures the proper attack sequence and allows the attacks to switch back and forth
        """
        if self.user_turn:
            print("\nYour Move!")
            self.user_fighter.showFighterMoves()
            try:
                attack = input("\nAttack with: ")
                attack_ix = self.user_fighter.fighting_moves.index(attack)
            except:
                print("The move you typed doesn't exist!")
            self.computer_fighter.health -= self.user_fighter.useMove(attack_ix)
            self.user_turn = False
        else:
            self.user_fighter.health -= self.computer_fighter.useMove(self.computerAttack())
            self.user_turn = True

    def computerAttack(self):
        """
        Function that takes the computer's health into consideration and output's
        an appropriate attack.
        """
        if self.computer_fighter.health > 60:
            return randint(0,1)
        elif self.computer_fighter.health < 20:
            return 2
        else:
            return randint(0,2)

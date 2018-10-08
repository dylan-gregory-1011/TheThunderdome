#!/usr/bin/env python
"""
Defines The Class for the fighter to be used in the battle royale game.
"""

from TheThunderdome import TheThunderdome
import os

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"






if __name__ == '__main__':
    while True:
        os.system('cls')
        thunderdome_game = TheThunderdome()
        keep_playing = thunderdome_game.battleRoyale()
        if keep_playing == 'N':
            break

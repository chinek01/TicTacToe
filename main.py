"""

Główny plik projektu Tic Tac Toe -> Kółko i krzyżyk
#100DaysOfCode with Python
Day: 83
Start date: 2023-06-28
Author: MC

"""

from time import sleep
import os

import art.art as art
from game.game import Game
from gamer.gamer import Gamer


def clear():

    # for windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


print(art.logo)
sleep(5)
clear()

# set game - set players
players = []

for n in range(2):
    print(art.set_player_name(n))
    players.append(Gamer(input("Name: ")))
    clear()


print(players[0].name, ' ', players[1].name)

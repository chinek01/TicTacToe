"""

Główny plik projektu Tic Tac Toe -> Kółko i krzyżyk
#100DaysOfCode with Python
Day: 83
Start date: 2023-06-28
Author: MC

"""

from time import sleep
from random import randint
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


p1_symbol = 'X'
p2_symbol = 'O'

flag_new_game = True

# print logo
print(art.logo)
sleep(3)
clear()

# set game - set players
print(art.set_player_name(1))
player_1 = Gamer(input("Name: "))
clear()

print(art.set_player_name(2))
player_2 = Gamer(input("Name: "))
clear()

# main app loop
while flag_new_game:

    # choice who player will be first
    first_move = randint(1, 2)

    # set symbols for players
    if first_move == 1:
        player_1.set_symbol(p1_symbol)
        player_2.set_symbol(p2_symbol)
    else:
        player_1.set_symbol(p2_symbol)
        player_2.set_symbol(p1_symbol)

    # init game class - if new game init new object :)
    my_game = Game()

    while not my_game.end_game_flag and not my_game.dead_heat_flag:

        print()
        print(f"""
    end_game flag: {my_game.end_game_flag}
    dead-heat flag: {my_game.dead_heat_flag}
    """)
        my_game.print_area_gui()

        if first_move == 1:
            # wait for player_1 move
            print(art.set_player_move(player_1.name, player_1.symbol))
            my_game.set_symbol_on_field(player_1.get_symbol(),
                                        int(input("Field: ")))

            if my_game.end_game_flag is True:
                player_1.increase_score()

            first_move = 2
        else:
            # wait for player_2 move
            print(art.set_player_move(player_2.name, player_2.symbol))
            my_game.set_symbol_on_field(player_2.get_symbol(),
                                        int(input("Field: ")))

            if my_game.end_game_flag is True:
                player_2.increase_score()
            first_move = 1

        clear()

    # new game question
    if input("Another game [Y/N]: ").upper() != 'Y':
        flag_new_game = False

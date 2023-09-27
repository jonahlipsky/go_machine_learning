import os
from sgfmill import sgf

if __name__ == '__main__':
    prefix = os.getcwd()
    path = prefix + "/generate_features/sgfs-by-date/2005/12/01"
    game_names = os.listdir(path)
    for game_name in game_names:
        with open(path + "/" + game_name, "rb") as f:
            game = sgf.Sgf_game.from_bytes(f.read())
            # print(game.get_size())
            # print(game.get_komi())
            # print(game.get_handicap())
            print(game.get_root())
            for node in game.get_main_sequence():
                print(node.get_move())




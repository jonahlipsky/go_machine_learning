import os
from sgfmill import sgf
from sgfmill.boards import Board

if __name__ == '__main__':
    prefix = os.getcwd()
    path = prefix + "/generate_features/sgfs-by-date/2007/11/05"
    game_names = os.listdir(path)
    for game_name in game_names:
        with open(path + "/" + game_name, "rb") as f:
            game = sgf.Sgf_game.from_bytes(f.read())
            # print(game.get_size())
            # print(game.get_komi())
            # print(game.get_handicap())
            # print(game.get_root())
            board = Board(game.get_size())
            # print(board)
            for i, node in enumerate(game.get_main_sequence()):
                if i == 0:
                    continue
                color, coords = node.get_move()
                if coords is None:
                    continue

                row, col = coords
                # print(f"{color}-{row}-{col}")
                board.play(row, col, color)
            
            black_final = board.area_score() + game.get_komi()
            if black_final > 0 and game.get_winner() == 'b':
                print('success black wins and they match')
            elif black_final < 0 and game.get_winner() == 'w':
                print('success white wins and they match')
            elif black_final == 0 and game.get_winner() == None:
                print('success it was a draw and they mathc')
            else:
                # print(game.get_handicap())
                # print(game.get)
                print(f"FAIL: black {black_final} winner {game.get_winner()}")
                # raise Exception("Error!")





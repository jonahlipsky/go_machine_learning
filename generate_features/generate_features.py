from sgfmill import sgf
import os
from csv import writer

class GenerateFeatures:
    def __init__(self, year: str, month: str, day: str, max_games_to_process=float('inf')) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.pathway = f"/Users/jonahlipsky/repos/go/sgfs-by-date/{self.year}/{self.month}/{self.day}"
        
    def fetch_all_game_file_names(self):
        games = []
        if os.path.isdir(self.pathway):
            print('pathway')
            games = os.listdir(self.pathway)
        else:
            print('not a pathway')
        
        return games
    
    def fetch_and_store_games(self, target_size):
        names = self.fetch_names_of_all_games_of_target_size(target_size)
        self.store_paths(names, target_size)

    
    def fetch_names_of_all_games_of_target_size(self, target_size):
        game_names = self.fetch_all_game_file_names()
        target_size_games = []
        for game_name in game_names:
            game_path = self.pathway + "/" + game_name
            with open(game_path, "rb") as f:
                game = sgf.Sgf_game.from_bytes(f.read())
                if game.get_size() == target_size:
                    target_size_games.append(game_name)
        
        return target_size_games

    def store_paths(self, game_names, target_size):
        if len(game_names) > 0:
            # note that this will write into any file that already exists
            with open(f"size_{target_size}_game_names/{self.year}/size_{target_size}.csv", 'a') as f_object:
                writer_obj = writer(f_object)
                
                for name in game_names:
                    writer_obj.writerow([self.year, self.month, self.day, name])
                f_object.close()
        else:
            print('no games')

if __name__ == '__main__':
    GF = GenerateFeatures('2005', '11', '05')
    GF.fetch_and_store_games(9)


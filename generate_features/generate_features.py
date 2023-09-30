from sgfmill import sgf
import os
from csv import writer
from feature_row import FeatureRow

class GenerateFeatures:
    def __init__(self, year: str, month: str, day: str, target_board_size: int) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.target_board_size = target_board_size
        prefix = os.getcwd() + "/generate_features/sgfs-by-date/"
        self.pathway = prefix + f"{self.year}/{self.month}/{self.day}"
        
    def fetch_all_game_file_names(self):
        games = []
        if os.path.isdir(self.pathway):
            print('pathway')
            games = os.listdir(self.pathway)
        else:
            print('not a pathway')
        
        return games
    
    def fetch_and_store_game_features_and_targets(self):
        games = self.fetch_games_of_target_size()
        self.generate_and_store_features(games)
    
    def fetch_games_of_target_size(self):
        game_names = self.fetch_all_game_file_names()
        target_size_games = []
        for game_name in game_names:
            game_path = self.pathway + "/" + game_name
            with open(game_path, "rb") as f:
                game = sgf.Sgf_game.from_bytes(f.read())
                if self.game_is_target_size(game):
                    target_size_games.append(game)
        
        return target_size_games

    def game_is_target_size(self, game):
        return game.get_size() == self.target_board_size

    def generate_and_store_features(self, games):
        if len(games) > 0:
            # note that this will write into any file that already exists
            prefix = ""
            for i, directory in enumerate([f"size_{self.target_board_size}_games", "v1", f"{self.year}"]):
                if i == 0:
                    prefix += directory
                else:
                    prefix += "/" + directory
                
                if not os.path.isdir(prefix):
                    os.mkdir(prefix)
                    
            file_name = f"{prefix}/{self.year}-features.csv"
            if not os.path.isfile(file_name):
                with open(file_name, 'a') as f_object:
                    writer_obj = writer(f_object)
                    writer_obj.writerow(FeatureRow.feature_headers('v1', self.target_board_size))
                    f_object.close()

            with open(file_name, 'a') as f_object:
                writer_obj = writer(f_object)
                
                for game in games:
                    feature_rows = FeatureRow(game, 'v1')
                    for row in feature_rows.list_of_feature_rows:
                        writer_obj.writerow(row)
                f_object.close()
        else:
            print('no games')


if __name__ == '__main__':
    GF = GenerateFeatures('2005', '11', '05', 9)
    GF.fetch_and_store_game_features_and_targets()


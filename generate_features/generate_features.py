from sgfmill import sgf
import os

class GenerateFeatures:
    def __init__(self, year: str, month: str, day: str, max_games_to_process=float('inf')) -> None:
        self.year = year
        self.month = month
        self.day = day


    def fetch_all_game_file_names(self):
        pathway = f"/Users/jonahlipsky/repos/go/sgfs-by-date/{self.year}/{self.month}/{self.day}"
        games = []
        if os.path.isdir(pathway):
            print('pathway')
            games = os.listdir(pathway)
            print(games)
        else:
            print('not a pathway')
        
        return games


    # def load_game(sgf_file_path):
        
if __name__ == '__main__':
    GF = GenerateFeatures('2005', '11', '05')
    GF.fetch_all_game_file_names()


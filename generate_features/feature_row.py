from sgfmill.boards import Board

class FeatureRow:
    def __init__(self, game, version):
        self.game = game
        self.version = version
        self.list_of_feature_rows = parse_features()

    @classmethod
    def num_features(cls, version, board_size):
        num_ranks = 78 # 30 kyu, 9 dan, for both black and white
        if version == 'v1':
            # num captures b/w, is_blacks_move (satisfies white too), and current turn
            num_non_board_related_features = 4
            
            return (board_size ^ 2) * 3 + num_ranks + num_non_board_related_features
        else:
            raise Exception('Not implemented.')
        
    @classmethod
    def feature_headers(cls, version, board_size):
        headers = []
        if version == 'v1':
            for row in range(board_size):
                for col in range(board_size):
                    headers.append(f"({row},{col})")
            for dan_rank in range(9, 0, -1):
                headers.append(f"{dan_rank}d")
            for kyu_rank in range(30, 0, -1):
                headers.append(f"{kyu_rank}k")
            for color in ['b', 'w']:
                 headers.append(f"{color}_captures")
            
            headers.append(f"is_blacks_move")
            headers.append("turn_count")
        else:
            raise Exception(f"Not implemented for version: {version}")

    def parse_features(self):
        if self.version == 'v1':
            return self.parse_features_v1()

    def parse_features_v1(self):
        n_features_and_output = [0 for _ in range(FeatureRow.num_features(self.version, self.game.get_size()))]
        board = Board(self.game.get_size())
        feature_rows = []
        game_sequence = self.game.get_main_sequence()
        for i, node in enumerate(game_sequence):
            row = []
            if i == 0:

            
            color, coords = node.get_move()
            
            if i == 1 and color != "b":
                raise Exception("Check your assumption that i == 0 is always a non-move.")



            if coords is None:
                continue

        for row in range(game.get_size()):
            for col in range(game.get_size()):

        

    
    
from sgfmill.boards import Board

class FeatureRow:
    @classmethod
    def num_features(cls, version, board_size):
        num_ranks = 78 # 30 kyu, 9 dan, for both black and white
        if version == 'v1':
            num_non_board_related_features = 1 # is_blacks_move (satisfies white too)
            board_size_move_features = (board_size ** 2) * 2
            target_features = (board_size ** 2) + 1 # one for each spot plus one for no move
            return board_size_move_features + target_features + num_ranks + num_non_board_related_features
        else:
            raise Exception('Not implemented.')
        
    @classmethod
    def feature_headers(cls, version, board_size):
        headers = []
        if version == 'v1':
            for color in ['b', 'w']:
                for row in range(board_size):
                    for col in range(board_size):
                        headers.append(f"feat_{color}_at_{row}_{col}")
            for color in ['b', 'w']:
                for dan_rank in range(9, 0, -1):
                    headers.append(f"feat_{color}_ranked_{dan_rank}d")
                for kyu_rank in range(30, 0, -1):
                    headers.append(f"feat_{color}_ranked_{kyu_rank}k")
            
            headers.append(f"feat_is_blacks_move")

            for row in range(board_size):
                for col in range(board_size):
                    headers.append(f"target_{row}_{col}_next_move")
            headers.append('target_no_move')
            return headers
        else:
            raise Exception(f"Not implemented for version: {version}")

    def __init__(self, game, version):
        self.game = game
        self.board_size = game.get_size()
        self.version = version
        self.list_of_feature_rows = self.parse_features()

    def parse_features(self):
        if self.version == 'v1':
            return self.parse_features_v1()

    def parse_features_v1(self):
        n_features_and_targets = FeatureRow.num_features(self.version, self.board_size)
        board = Board(self.board_size)
        feature_rows = []
        game_sequence = self.game.get_main_sequence()
        root = self.game.get_root()
        property_map = root.get_raw_property_map()
        black_rank = property_map['BR']
        white_rank = property_map['WR']

        for node in game_sequence:
            if node == root:
                continue

            one_row = [0 for _ in range(n_features_and_targets)]
            
            num_black_stones = 0
            num_white_stones = 0

            cur_feature = 0

            # fill out stones features for current state
            for color in ['b', 'w']:
                for row in range(self.board_size):
                    for col in range(self.board_size):
                        stone_color_or_none = board.get(row, col)
                        if stone_color_or_none == col:
                            one_row[cur_feature] = 1

                            if col == 'b':
                                num_black_stones += 1
                            else:
                                num_white_stones += 1    
                        
                        cur_feature += 1
            
            
            # fill out rank positions
            for color in ['b', 'w']:
                for dan_rank in range(9, 0, -1):
                    if color == 'b' and f"{color}'{dan_rank}'d" == black_rank:
                        one_row[cur_feature] = 1
                    elif color == 'w' and f"{color}'{dan_rank}'d" == white_rank:
                        one_row[cur_feature] = 1

                    cur_feature += 1
                    
                for kyu_rank in range(30, 0, -1):
                    if color == 'b' and f"{color}'{kyu_rank}'k" == black_rank:
                        one_row[cur_feature] = 1
                    elif color == 'w' and f"{color}'{kyu_rank}'k" == white_rank:
                        one_row[cur_feature] = 1

                    cur_feature += 1

            # fill out features for target
            current_move_color, cur_move_coords = node.get_move()

            if current_move_color == 'b':
                one_row[cur_feature] = 1

            cur_feature += 1

            if cur_move_coords == None:
                one_row[-1] = 1

                # because the move wasn't on any of the coordinates, 
                # which are the reset of the features
                feature_rows.append(one_row)
                continue
            
            cur_move_row, cur_move_col = cur_move_coords
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if row == cur_move_row and col == cur_move_col:
                        one_row[cur_feature] = 1
                    
                    cur_feature += 1

            feature_rows.append(one_row)
    
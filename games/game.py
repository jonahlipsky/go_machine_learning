import pickle
class Game:
  def __init__(self, game, number) -> None:
    self.game_number = number
    self.game = game
    

  def dump_game(self):
    game = str(self.game)
    if self.game_size(game) == 9 and self.game_ends_in_two_passes(game):
      with open('game_dumps/' + str(self.game_number) + '.pk1', 'wb') as file:
        pickle.dump(self.game,file)
      return True
    else:
      return False
      
  def game_ends_in_two_passes(self, game):
    last_two = game.split('(')[-2:]
    return self.is_pass_move(last_two[0]) and self.is_pass_move(last_two[1])
  
  def game_size(self, game):
    i = game.index("SZ[")
    size = game[i+3:i+5].replace("]", "")
    return int(size)
  
  def is_pass_move(self, input_string):
    i = input_string.index('[')
    return input_string[i+1] == ']'

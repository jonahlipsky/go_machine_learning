import pickle
class Game:
  def __init__(self, game, number) -> None:
    self.game_number = number
    self.game = game
    

  def dump_game(self):
    game = str(self.game)
    if self.game_size_is_nine(game) and self.game_ends_in_two_passes(game):
      with open('game_dumps/' + str(self.game_number) + '.pk1', 'wb') as file:
        pickle.dump(self.game,file)
      return True
    else:
      return False
      
  def game_ends_in_two_passes(self, game):
    last_two = game.split('(')[-2:]
    # Note that this is not always going to work. Sometimes the games
    # are not structured like this. See 57165691.
    return self.is_pass_move(last_two[0]) and self.is_pass_move(last_two[1])
  
  def game_size_is_nine(self, game):
    # Changed this to target nines because there's a five option that 
    # had a colon like '5:'. Maybe bad data?
    i = game.index("SZ[")
    size = game[i+3:i+5].replace("]", "")
    return size == "9"
  
  def is_pass_move(self, input_string):
    # Note sometimes there are formats that don't conform to the standard.
    # Something to look into. See 57165691
    try:
      i = input_string.index('[')
      return input_string[i+1] == ']'
    except:
      return False
  
    

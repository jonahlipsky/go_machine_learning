import http.client
from game import Game
import time
import pickle
import os

ANCHOR = 57166015

if __name__ == '__main__':
  target_games = 3000
  downloaded_games = 0
  
  thousands = 0

  cur_game = ANCHOR

  if os.path.isfile('./search_state.pk1'):
    with open('search_state.pk1', 'rb') as file:
      cur_game, target_games, downloaded_games, thousands = pickle.load(file)
  
  print(f"cur_game: {cur_game}")
  while downloaded_games < target_games:
    connection = http.client.HTTPSConnection("online-go.com")
    connection.request("GET", "/api/v1/games/" + str(cur_game) + "/sgf")
    response = connection.getresponse()

    if response.status == 200:
      game = Game(response.read(), cur_game)
      if game.dump_game():
        downloaded_games += 1

        if downloaded_games % 100 == 0:
          print(f"100 games: {downloaded_games}")
    
    with open('search_state.pk1', 'wb') as file:
      pickle.dump([cur_game, target_games, downloaded_games, thousands],file)    
    
    cur_game -= 1

    if cur_game % 1000 == 0:
      thousands += 1
      print(f"1000s: {thousands} at {time.localtime().tm_hour}:{time.localtime().tm_min}")


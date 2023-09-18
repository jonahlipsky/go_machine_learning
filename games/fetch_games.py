import http.client
from game import Game
import time
import pickle
import os

ANCHOR = 57166015

if __name__ == '__main__':
  target_games = 3
  downloaded_games = 0
  hundreds = 0
  thousands = 0
  cur_game = ANCHOR
  if os.path.isfile('./search_state.pk1'):
    with open('search_state.pk1', 'rb') as file:
      cur_game, target_games, downloaded_games, hundreds, thousands = pickle.load(file)
  
  while downloaded_games < target_games:
    connection = http.client.HTTPSConnection("online-go.com")
    connection.request("GET", "/api/v1/games/" + str(cur_game) + "/sgf")
    response = connection.getresponse()
    if response.status == 200:
      print("hi")
      game = Game(response.read(), cur_game)
      if game.dump_game():
        downloaded_games += 1
    
    cur_game -= 1

    if cur_game % 100 == 0:
      hundreds += 1
      print(f"100s: {hundreds} at {time.localtime().tm_hour}:{time.localtime().tm_min}")
    if cur_game % 1000 == 0:
      thousands += 1
      print(f"1000s: {thousands} at {time.localtime().tm_hour}:{time.localtime().tm_min}")
    time.sleep(0.2)
  with open('search_state.pk1', 'wb') as file:
    pickle.dump([cur_game, target_games, downloaded_games, hundreds, thousands],file)

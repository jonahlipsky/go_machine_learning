# Neural Net Architecture

## Feature List

81 for "is_black"
81 for "is_white"
30 for 30k - 1k black
9 for 1d - 9d black
30 for 30k - 1k white
9 for 1d - 9d white
1 for is_blacks_move

Altogether 241 features.
We need to include 82 output columns as we parse the game, as well: one for each position and one for "NoMove". 
So 241 + 82 = 323 columns

I'm not including the black captures and white captures because to do so would involve taking the handicap into account. Points, Komi, and the Handicap should probably be V2. I'm also letting turn of the game be V2 since that is also a continuous variable. 


### Possible neural network architecture.

For starters, let there be one hidden layer of 100 nodes and 81 output nodes -- one for each position.
This'll be a starting point to see how well it performs out of the box.

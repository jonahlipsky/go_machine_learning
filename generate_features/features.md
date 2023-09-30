# Neural Net Architecture

## Feature List

81 for "is_black"
81 for "is_white"
30 for 30k - 1k black
9 for 1d - 9d black
30 for 30k - 1k white
9 for 1d - 9d white
1 for which move of the game we're on.
1 for black captures
1 for white captures
1 for is_whites_move
1 for is_blacks_move

Altogether 245 features.
We need to include 82 output columns as we parse the game, as well: one for each position and one for "NoMove". 
So 245 + 82 = 327 columns

### Possible neural network architecture.

For starters, let there be one hidden layer of 100 nodes and 81 output nodes -- one for each position.
This'll be a starting point to see how well it performs out of the box.

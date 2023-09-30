# Design Ideas for a Deep Neural Network

## Assumptions
- Limited to a 9x9 game board for now
- Usernames will not be a feature at first so there is no direct user-by-user bias

## Output
one vs all approach
81 outputs for each place on the board
1 output for pass
1 output for resign

## Input
Features:
- My rank
- Opponent's rank
- My score
- Opponent's score
- Komi (or is Komi just added to the score)
- Ko if there's a way to represent Ko as a feature. Would it be a "would be Ko" yes/no feature for every space on the board?
- There might be a "would be legal" feature for every space on the board that takes into account Ko, Suicidal moves, and moving onto a piece that 
already is played.
- The current turn number
- The degrees of freedom of all my groups in quadrant one (if there were 5 quadrants -- each corner and a 5x5 in the middle)
- Same as above but for opponent
- The number of pieces played by me in each quadrant over the past 3 moves
- The number of pieces played by me in each quadrant over the past 10 moves
- The same, but for just the last move
- The same as the three above, but 

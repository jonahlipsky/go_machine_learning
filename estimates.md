# Estimates

## Estimate on downloading complete history of go games.

Note: After doing these estimates, it became clear that this would take maybe too long.
Apparently, the rate limiting that online-go imposes would make it take even longer.
However, there was an online archive of all games leading up to 2021. Expanding it was taking too long,
though, so I could equivalently gather the last 3000 matches or so and start working with the data on a 
much smaller data set. That'd allow the code to go fast and then when I am ready I can train the whole model.

### Space to hold all the game states
Assuming that one game state is 1000 bytes (10^3)
There are on the order of 100 million games (10^8)
10^8 * 10^3 = 10^11 bytes
Converting bytes into gigabtyes:
10^11 bytes * ( 1 gigabyte / 10^9 bytes) = 10^2 gigabytes

### Time to query all the game states
Assuming that the query and save to disk operation takes on the order of 
100 ms
10^8 * 10^2 ms = 10^10 ms
Converting this to seconds
10^10 ms * (1 second / 10^3 ms) = 10^7 seconds
Seconds in a day is 86400 so we will say on the order of 10^5 seconds in 
a day
Converting to days
10^7 * ( 1 day / 10^5 seconds) = 100 days

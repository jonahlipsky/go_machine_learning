# Download Approach

- I had intended to download 3000 games, but I ended up downloading 1000 and for testing that probably is plenty.

## Notes

- There were a few occassionally occurring errors that suggest the response objects are sometimes structured a little differently.
- I ultimately searched through 70,000 games in order to find 1000 9x9 where the games ended in two pass moves.
- The Game class handles parsing the raw game response and determining if it's 9x9 and ends in two passes. It also handles dumping the stringified filed into a pickle dump.
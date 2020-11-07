# RookJumpingMaze

This project is based off a Jump Maze. A Jump maze is a n by n 2D array with each index having a jump number. A jump number is a number that states how many steps away it can take. For example

A 3 x 3 jump maze

2 2 1 

2 1 2 

1 1 0 


0, is the goal state, and we start at the top left node which has the number "2". It can only go horizontal and vertical like a rook piece in chess. From there, it has to try to find its way to the goal in the shortest amount of steps.

To solve this, I created an artificial intelligence that solves the maze in the shortest amount of steps. 

part1 = Creates an n by n Jump Maze desired by the user

part2 = Finds the shortest amount of steps to each index from a random 5x5 jump maze

part3 = For a certain number of iterations, it creates a random jump maze until it finds the most fun one.

part4 = Part3 but it uses random restarts for more accuracy

part5 = Part3 but it uses probability to escape local minima

part6 = Part3 but it uses simulated annealing.

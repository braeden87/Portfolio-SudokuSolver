# Sudoku Solver
## Skills Utilized
- Python
- Pygame
- Backtracking Algorithm
## Project Description
The Sudoku Solver project takes a sudoku puzzle, and utilizes the backtracking algorithm to solve all of the blank squares inside of the puzzle. I created this project using Python and then added a GUI to the project using Pygame. 

The program allows the user to click on any empty square in the puzzle and enter a number between 1 and 9. If the number entered is correct, then it will get added to the puzzle. If the guess is incorrect, then a red X will display in the lower left corner and the number entered will dissapear. Whenever the user decides they are done trying to solve the puzzle, they can hit spacebar and the program will begin to solve the remaining blank spaces. It starts in the top left and taverses left to right, row by row, until it reachs the end. 

If you watch the program run you can see the Backtracking Algorithm in action as the program will at times get to a certain point, realize that the answer is not possible, and will set the current value back to blank, or 0, and will attempt to find a new value that works for the previos blank space.

## Inspiration For Project Creation
I was initially motivated to create this project after hearing about it from Tim Ruscica (can be found on GitHub at techwithtim) on his youtube channel. He created it himself years ago, and recommended it as a great way to showcase your proficciency with python. After seeing and hearing about the project, I was intrigued by how it all actually worked and decided to create my own version. 
## Project In Action
https://user-images.githubusercontent.com/59823288/139083531-559a715b-26ee-449f-a16a-95a0c812314f.mp4


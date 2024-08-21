# LinkedIn Queens Solver

## The Game

An `n x n` chess board contains cells belonging to colour regions.

The objective of the game is to place `n` queens on the board such that there is exactly one queen in each row, column, and colour region.

Two queens cannot touch each other, even diagonally.

## The Solver

The solver makes use of a backtracking algorithm. Starting with the first row, we place a queen in the first available 'safe' square (where the placement obeys the rules), and then recursively call the `solveLinkedInQueens` function, moving to the next row.

In the event that no legal square exists in that row given the current board state, we backtrack, resetting the previous placement and moving to the next 'safe' cell.

Once a queen has been placed in every row, we check if the colour region rules are obeyed. If so, we have the solution. If not, we backtrack again.

## Archive

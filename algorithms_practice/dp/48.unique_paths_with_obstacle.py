'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

# def unique_paths_two(grid):
#     if grid[0][0] == 1: return 0
#     grid[0][0] = 1
#
#     for i in range(1, len(grid[0])):
#         grid[0][i] = 0 if grid[0][i] == 1 else grid[0][i-1]
#
#     for i in range(1, len(grid)):
#         grid[i][0] = 0 if grid[i][0] == 1 else grid[i-1][0]
#
#
#     for i in range(1, len(grid)):
#         for j in range(1, len(grid[0])):
#             if grid[i][j] == 1: grid[i][j] = 0
#             else: grid[i][j] = grid[i-1][j] + grid[i][j-1]
#
#     return grid[-1][-1]
from algorithms3.dp import unique_paths_with_obstacle
a=[
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(unique_paths_with_obstacle.unique_paths_two(a))
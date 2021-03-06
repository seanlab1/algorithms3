'''
Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with 
two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the 
operations.

Example 1:
Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.
'''

# def range_addition(m, n, ops):
#     for op in ops:
#         m = min(m, op[0])
#         n = min(n, op[1])
#
#     return m * n

def range_addition_v2(m, n, ops):
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    for element in ops:
        a, b = element[0], element[1]
        for i in range(a):
            for j in range(b):
                matrix[i][j] += 1

    max_seen_so_far = matrix[0][0]
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] > max_seen_so_far:
                max_seen_so_far = matrix[i][j]
                count = 1
            elif matrix[i][j] == max_seen_so_far:
                count += 1

    return count 

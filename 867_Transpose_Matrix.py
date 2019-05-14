'''
867. Transpose Matrix
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

TIME COMPLEXITY: O(ROW * COL)
SPACE COMPLEXITY:O(ROW * COL)

IDEA: 
[[1,2,3],
[4,5,6],      
[7,8,9]]

=> 

[[1,4,7],  
[2,5,8],
[3,6,9]]

i=0, j=0 swap with i=0, j=0 
i=0, j=1 swap with i=1, i=0
i=0, j=2 swap with i=2, j=0

i=1, j=1 swap with i=1, j=1
i=1, j=2 swap with i=2, j=1

i=2 j=2 swap with i=2, j=2
'''

'''
A: 
[[1,2,3,7],
[4,5,6,8]]

=> 
B: 
[[1,4],
[2,5],
[3,6]]

Iterate through the matrix A, with in following fashion in row, col order (idx) and populate matrix B 
0, 0
1, 0 

0, 1
1, 1

0, 2
1, 2
'''

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        #rows of A and cols of A 
        rows = len(A)
        cols = len(A[0])
        
        M = [[None] * (rows) for x in range(cols)] 
        
        for i in range(0, len(M)): 
            for j in range(0, len(M[0])): 
                print(A[j][i])
                M[i][j] = A[j][i]
                
        return M

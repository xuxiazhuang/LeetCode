Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


solution1:
  list1=[]
        for col in zip(*A):
            col=list(col)
            list1.append(col)
        return(list1)
   or   return(zip(*A))     
solution2:
R = len(A)
C = len(A[0])
transpose = []
for c in range(C):
	newRow = []
	for r in range(R):
		newRow.append(A[r][c])
	transpose.append(newRow)
return(transpose)

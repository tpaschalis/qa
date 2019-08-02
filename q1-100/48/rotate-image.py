class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Reverse -90deg
        #for i in range(n):
        #    matrix[i] = matrix[i][::-1]
        #for i in range(n):
        #    for j in range(i):
        #        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse 90deg
        #matrix = matrix.reverse()
        #for i in range(int(n/2)):
        #    matrix[i], matrix[n - i -1] = matrix[n-i-1], matrix[i]
        #for i in range(n):
        #    for j in range(i):
        #        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        matrix[::] = zip(*matrix[::-1])
        matrix[:] = [ [row[i] for row in matrix[::-1]] for i in range(len(matrix))]


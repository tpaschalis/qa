
# Pythonic Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # At each step, you take the first row, transpose the matrix and reverse it
        # It's the same as rotating the matrix counter-clockwise
        # You need to reverse the matrix of n elements, at least 2*n -1 times.
        # So it's O(n^2)
        # So, it would be :
        #[1, 2, 3, 4],      <-- result.append()
        #[5, 6, 7, 8],
        #[9,10,11,12]
        
        # [8, 12],          <-- result.append()
        # [7, 11],
        # [6, 10],
        # [5, 9]
        
        # [11, 10, 9]       <-- result.append()
        # [7, 6, 5]
        
        # [5, 6, 7]         <-- result.append()
        
        res = []
        while len(matrix)>0:
            #res = res + [*matrix.pop()] + self.spiralOrder([*zip(*matrix)][::-1])
            res += matrix.pop(0)
            matrix = [*zip(*matrix)]
            matrix = matrix[::-1]
        return res


## Straightforward solution, walk around matrix and turn whenever you encountered a boundary or something you've already seen
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
            if matrix == []:
                return []

            rows, cols = len(matrix), len(matrix[0])

            seen, res = [], []
            for i in range(rows):
                seen.append([False] * cols)

            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]

            row = col = direction = 0

            for _ in range(rows * cols):
                res.append(matrix[row][col])        # Or `col * row + col`, if we have a flattened matrix
                seen[row][col] = True
                current_row, current_col = row + dr[direction], col + dc[direction]
                if 0 <= current_row < rows and 0 <= current_col < cols and seen[current_row][current_col] == False:
                    row, col = current_row, current_col
                else :
                    direction = (direction + 1) % 4
                    row, col = row + dr[direction], col + dc[direction]
            return res


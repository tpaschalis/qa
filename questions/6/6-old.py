class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = []
        n = len(s)
        
        if numRows == 1 or numRows>=n :
            return s
        
        # First row
        for i in range(0, n, 2 * (numRows - 1)):
            print("first", s[i])
            res.append(s[i])

        # Middle rows
        for i in range(1, numRows - 1):
            for j in range(0, len(s)+1, 2 * numRows-2):
                #print(i, j, j-i, j+i, s[j-i], s[j+i])

                if j-i > 0 and j-i < len(s):
                    res.append(s[j-i])
                if j+i< len(s):
                    res.append(s[j+i])
        
        # Final row            
        for i in range(numRows-1, n, 2 * (numRows - 1)):
            print("last", s[i])
            res.append(s[i])

        
        return ''.join(res)

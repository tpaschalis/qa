class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        res = [''] * numRows
        idx, step = 0, 1
        for letter in s:
            res[idx] += letter
            if idx == 0 :
                step = 1
            if idx == numRows -1 :
                step = -1
            
            idx += step
        return ''.join(res)

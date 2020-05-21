class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mappings = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
        }
        
        #res = [""] if digits != "" else []
    
        if len(digits) != 0 :
            res = [""]
        else:
            res = []
            
        for i in digits:
            current = list()
            for comb in res:
                for letter in mappings[i]:
                    current.append(comb + letter)
            res = current
        return res
        
# Nice one-liner from a stranger
# from functools import reduce
# return reduce(lambda curr, digit: [x + y for x in curr for y in mappings[digit]], digits, [""])
#
# Runs in the same time, as it"s the same idea under the hood.

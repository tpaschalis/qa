class Solution:
    def intToRoman(self, num: int) -> str:
        maps = {
        0 : ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        1 : ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        2 : ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        3 : ["", "M", "MM", "MMM"]
        }
        i = 0
        res = ""
        while num > 0:
            curr = num % 10
            res = maps[i][curr] + res
            num = int(num/10)
            i += 1
        return res

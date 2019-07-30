
# No recursion, regex
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = "1"
        for i in range(n-1):
            splits = [m.group(0) for m in re.finditer(r"(\d)\1*", res)]
            res = ""
            for i in splits:
                res = res + str(len(i)) + str(i[0])
        return res

# Use itertools.groupby
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        seq, res = "1", "1"

        for _ in range(n-1):
            res = ""
            # Iterate the sequence, grouped by digits
            for digit, group in itertools.groupby(seq):
                count = len(list(group))                # eg. the 3 in "three ones"
                res = res + "%i%s" % (count, digit)     # gather the 31 string
            seq = res
        return res


# Homemade say_it_loud function as well
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        seq, res = "1", "1"
        
        def say_it_loud(string: str) -> str:
            res, count = "", 1
            string += "#"
            for i in range(len(string)-1):
                if string[i] == string[i+1]:
                    count += 1
                else :
                    res += str(count) + string[i]
                    count = 1
            return res

        for _ in range(n-1):
            res = say_it_loud(res)
            
        return res

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left = 0
        right = n
        
        while left < right:
            mid = int((left + right)/2)
            # mid = left + (right - left) / 2; to avoid overflows
            if isBadVersion(mid):
                right = mid
            else :
                left = mid+1
        return left

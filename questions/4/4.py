class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
	# Take advantage of the fast built-in operations Python has
	# Will develop the more intricate, clever solution as well
        x = nums1 + nums2
        n = len(x)
        x = sorted(x)
        if n < 1:
            return(None)
        if n % 2 == 1:
            return(x[n//2])
        else:
            return(sum(x[(n//2)-1 : (n//2)+ 1]) / 2.0)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(n: List[int], start: int) -> None:
            i, j = start, len(n)-1
            while i < j:
                n[i], n[j] = n[j], n[i]
                i += 1
                j -= 1

                
        i = len(nums) - 2
        while i >=0 and nums[i+1] <= nums[i]:
            i -= 1
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
	# This also takes care of the edge case; 
	# if all input is in descending order, 
	# (i.e. is the greatest permutation available)
	# it returns the reverse, the smallest lexographic permutation as well.
        reverse(nums, i+1)
        return nums




#                     nums = [ 1, 3, 4, 5, 6, 9 ]
# `i` will run this way                <----- i 
# and will find the rightmost pair where i+1 will be greater than i
# since all numbers *after* a[i-1] are in descending order, we cannot create a larger permutation with them.
#
# So, we need to rearrange the numbers from a[i-1] (inclusive), to a[len(a)]
# 
# The permutation that will be *just* the next larger one, is the one that replaces a[i-1] with the next greater number to its right. This will be a[j].
#
# We're not ready yet. We need to create the *next larger* lexographic permutation. 
# We did a good first step swapping a[i] and a[j], but we still need to reverse all numbers *to the right of a[i-1]*. 
# They were in descending order, we need to have them in ascending order, to get the *just greater* permutation


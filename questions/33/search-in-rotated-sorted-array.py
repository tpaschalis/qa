
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            #mid = int(left + (right - left)/2)
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            
            # Left Half is sorted, pivot is on the right
            if nums[left] <= nums[mid]:
                
                # If the target is in the left half, continue the binary search there;
                # else, reverse the search, making the left equal to mid
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else :
                    left = mid + 1
            # Right Half is sorted, pivot is on the left
            else :
                
                # If the target is in the right half, continue the binary search there;
                # else, reverse the search, making the right equal to the mid
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else :
                    right = mid - 1
                    
        return -1



# ROFL, for some reason Leetcode times this linear O(n) solution faster than the 
# O(logn). Bad test cases? :P 
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target:
                return l
            else:
                l+=1 
            if nums[r] == target:
                return r
            else:
                r-=1
        return -1


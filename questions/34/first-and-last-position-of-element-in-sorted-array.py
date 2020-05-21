
# Python bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0 or nums is None:
            return [-1, -1]
        
        left = bisect.bisect_left(nums, target)
        
        if left > len(nums) - 1:
            return [-1, -1]
        
        right = bisect.bisect_right(nums, target)
        
        if nums[right - 1] == target:
            return [left, right -1]
        
        return [-1, -1]

# Straight Binary Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def insertion_index(nums: List[int], target: int, left: bool) -> int:
            lo = 0
            hi = len(nums)
            
            while lo < hi :
                mid = int( (lo + hi)/2 )
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid+1
            return lo
        
        target_range = [-1, -1]
        
        left_idx = insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return target_range
        
        target_range[0] = left_idx
        target_range[1] = insertion_index(nums, target, False) - 1
        
        return target_range

# Python built-ins
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = [-1, -1]
        
        try: 
            res[0] = nums.index(target)
        except :
            return [-1, -1]
        nums = nums[::-1]
        res[1] = len(nums) - nums.index(target) -1
        return res

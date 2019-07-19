class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        for i in nums[1:]:
            if i != nums[pos]:
                pos+=1
                nums[pos] = i

        # "It doesn't matter what you return after the length of the array"
        # nums = nums[:pos+1]
        return pos+1

# More Verbose
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         N = len(nums)
#         
#         if N<= 1:
#             return N
#         
#         pos = 0
#         last_seen = nums[pos]
# 
#         for i in range(N):
#             if last_seen == nums[i]:
#                 continue
#             else:
#                 pos +=1 
#                 last_seen = nums[pos] = nums[i]
#                 
#         return pos+1

# Not much better
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
# 
# 
#         pos = 0
#         for i in nums[1:]:
#             if i != nums[pos]:
#                 pos+=1
#                 nums[pos] = i
#                 
#         return pos+1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl not in d.keys():
                d[nums[i]] = i
            else:
                return[i, d[compl]]
            

#
# Runtime: 36 ms, faster than 89.82% of Python3 online submissions for Two Sum.
# Memory Usage: 14.4 MB, less than 36.74% of Python3 online submissions for Two Sum.
#
# Three basic approaches
# 1. Brute-force the entire thing - O(n^2) in time, O(1) in space
# 2. Use a hash table/dictionary/map, which is nearly O(1) in time, and O(2*n)/O(n) in space.
# This can happen in either two passes, where you fill the map, and then look for the complement
# Or in one pass, where you look for the complement as you're filling it
#
# NOTE : Initially I tried dict[index] = value, but made things too cumbersome, dict[value] = index allowed
# for easy lookups and such a simple solution


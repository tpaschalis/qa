class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # I first was comparing to the 'max' value
        # But if we have k positive numbers, if a missing positive exists it must be between [1, k+1]
        
        # Non-constant space, though
        present = set()
        for i in nums:
            if i not in present and i > 0:
                present.add(i)
          
        for i in range(1,len(nums)+2):
            if i not in present:
                return i
        
        
        # For anyone who doubts on the complexity of this algorithm: just consider position with A[i] = i+1 as a CORRECT SLOT.

        # CORRECT SLOT will never be changed: for CORRECT SLOT, A[A[i] - 1] always equals to A[i], vice versa (1)
        # For each swap, the number of CORRECT SLOT increases by at least 1: Position A[A[i] - 1] = A[i] becomes a CORRECT SLOT after swap, and according to (1), this must be a new CORRECT SLOT
        # The maximum of CORRECT SLOT <= N
        # We visit each number once, and each number will be put in its right place at most once, so it is O(n) + O(n). Although there are two nesting of cyclic (for and while), but its time complexity is still O(n).
        # Therefore, the complexity is O(N)
        
        n = len(nums)
        for i in range(n):
            digit = nums[i]
            while 0 < digit <= n and nums[digit-1] != digit:
                    nums[i], nums[digit-1] = nums[digit-1], nums[i]
                    digit = nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
    
    
        # This solution is smart, but destroys the initial array
        # The basic idea is that again, for a length k array, the first missing positive is between [1, k+1], so we only need to keep these elements in mind
        # Also, we can use the array index to stroe the frequency of each number within that [1, k+1] range
        
        # In case that an empty array is provided
        nums.append(0)
        
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        # Magic sause. use nums[i] as the hash to store the frequency of each number
        for i in range(n):
            nums[nums[i]%n] += n
    
        for i in range(1, n):
            if int(nums[i]/n) == 0:
                return i
        return n

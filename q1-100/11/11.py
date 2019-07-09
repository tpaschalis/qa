class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height) - 1
        max_bucket = 0
        
        while left != right :
            current_bucket = min(height[left], height[right]) * (right - left)
            max_bucket = max(max_bucket, current_bucket)
            if height[left] <= height[right]:
                left += 1
            else :
                right -= 1
                
        return max_bucket
        
        # Brute Force
        #maxbucket = 0
        #for p1, i in enumerate(height):
        #    for p2, j in enumerate(height):
        #        current_bucket = min(i, j) * (p2 - p1)
        #        maxbucket = max(maxbucket, current_bucket)
        #return(maxbucket)
        

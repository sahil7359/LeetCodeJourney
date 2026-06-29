class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = float('-inf') 
        
        # current sum of subarray
        sum = 0 
        
        # Iterate through the array
        for i in range(len(nums)):
            
            # Add current element to the sum
            sum += nums[i] 
            
            # Update maxi if current sum is greater
            if sum > maxi:
                maxi = sum 
            
            # Reset sum to 0 if it becomes negative
            if sum < 0:
                sum = 0 
        
        # Return the maximum subarray sum found
        return maxi
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        for i in range(n/2):
            nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
        for i in range(k,(n+k)/2):
            nums[i],nums[n+k-i-1]=nums[n+k-i-1],nums[i]
        for i in range(k//2):
            nums[i],nums[k-i-1]=nums[k-i-1],nums[i]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l=0
        for i in range(n):
            if nums[i]!=0:
                nums[l]=nums[i]
                l+=1
        for i in range(n-l):
            nums[l]=0
            l+=1
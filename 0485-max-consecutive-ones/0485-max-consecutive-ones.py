class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev=0
        ans=0
        for i in range(len(nums)):
            if nums[i]!=1:
                prev=0
            else:
                prev+=1
                ans=max(prev,ans)

        return ans
        
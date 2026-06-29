class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xorr = 0
        for i in nums:
            xorr^=i
        return xorr
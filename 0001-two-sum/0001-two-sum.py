class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        preInd = {}
        for i in range(n):
            rem = target-nums[i]
            if rem in preInd:
                return [preInd[rem],i]
            
            preInd[nums[i]]=i
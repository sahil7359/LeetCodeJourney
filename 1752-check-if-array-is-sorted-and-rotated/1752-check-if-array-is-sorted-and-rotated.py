class Solution(object):
    def check(self, nums):
        n = len(nums)
        rotates=0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotates+=1
                if rotates>1:
                    return False

        return True
        
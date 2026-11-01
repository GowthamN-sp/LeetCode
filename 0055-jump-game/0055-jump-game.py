class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far=0
        n=len(nums)
        for i in range(n):
            if i>far:
                return False
            reach=i+nums[i]
            far=max(reach,far)
            if far>=n-1:
                return True 
        return True
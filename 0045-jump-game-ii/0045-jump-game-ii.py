class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        far=0
        curr_end=0
        jump=0
        for i in range(len(nums)-1):
            reach=i+nums[i]
            far=max(reach,far)
            if i==curr_end:
                jump+=1
                curr_end=far
        return jump
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in d:
                return (d[com],i)
            d[nums[i]]=i
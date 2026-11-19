class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        contain=set(nums)
        longest=0
        for num in contain:
            if num-1 not in contain:
                count=1
                current=num
                while current+1 in contain:
                    count+=1
                    current+=1
                longest=max(count,longest)
        return longest

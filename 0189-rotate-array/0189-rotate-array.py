class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def tilt(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        tilt(nums,0,n-k-1)
        tilt(nums,n-k,n-1)
        tilt(nums,0,n-1)
        return nums
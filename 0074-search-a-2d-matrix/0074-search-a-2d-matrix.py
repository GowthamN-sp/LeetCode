class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left=0
        r=len(matrix)
        c=len(matrix[0])
        right=r*c-1
        while left<=right:
            mid=(left+right)//2
            row=mid//c
            col=mid%c
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                left=mid+1
            else:
                right=mid-1
        return False


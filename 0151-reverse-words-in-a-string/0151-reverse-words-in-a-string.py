class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        out=s.split()
        left=0
        right=len(out)-1
        while left<right:
            out[left],out[right]=out[right],out[left]
            left+=1
            right-=1
        return " ".join(out)
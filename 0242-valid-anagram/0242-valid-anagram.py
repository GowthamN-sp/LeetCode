class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for ch in t:
            if d.get(ch,0)==0:
                return False
            d[ch]-=1
        return True

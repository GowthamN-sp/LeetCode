class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for ch_s,ch_t in zip(s,t):
            if (ch_s in d1 and d1[ch_s]!=ch_t) or (ch_t in d2 and d2[ch_t]!=ch_s):
                return False
            d1[ch_s]=ch_t
            d2[ch_t]=ch_s
        return True
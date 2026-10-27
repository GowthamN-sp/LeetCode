class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        total=0
        for i in range(1,len(s)):
            if roman[s[i]]>roman[s[i-1]]:
                total-=roman[s[i-1]]
            else:
                total+=roman[s[i-1]]
        total+=roman[s[-1]]
        return total


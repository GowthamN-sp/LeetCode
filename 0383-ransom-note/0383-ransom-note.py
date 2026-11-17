class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)>len(magazine):
            return False
        d1={}
        d2={}
        for ch in ransomNote:
            d1[ch]=d1.get(ch,0)+1
        for ch in magazine:
            d2[ch]=d2.get(ch,0)+1
        for ch in d1:
            if d2.get(ch,0)<d1[ch]:
                return False
        return True
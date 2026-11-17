class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split()
        if len(pattern)!=len(words):
            return False
        d={}
        w={}
        for ch,word in zip(pattern,words):
            if ch in d and d[ch]!=word:
                return False
            if word in w and w[word]!=ch:
                return False
            d[ch]=word
            w[word]=ch
        return True
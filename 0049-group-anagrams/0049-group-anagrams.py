class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for word in strs:
            pat="".join(sorted(word))
            if pat in d:
                d[pat].append(word)
            else:
                d[pat]=[word]
        return list(d.values())
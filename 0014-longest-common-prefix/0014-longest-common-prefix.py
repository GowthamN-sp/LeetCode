class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        pre=strs[0]
        for s in strs[1:]:
            while not s.startswith(pre):
                pre=pre[:-1]
                if not pre:
                    return ""
        return pre
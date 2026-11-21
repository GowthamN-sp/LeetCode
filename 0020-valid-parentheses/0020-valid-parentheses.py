class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pair={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in pair.values():
                stack.append(ch)
            else:
                if not stack or stack.pop()!=pair[ch]:
                    return False
        return len(stack)==0
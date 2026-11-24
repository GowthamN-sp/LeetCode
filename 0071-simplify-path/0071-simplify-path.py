class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        for each in path.split("/"):
            if each=="" or each==".":
                continue
            elif each=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(each)
        return "/"+"/".join(stack)
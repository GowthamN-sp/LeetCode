class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for ch in tokens:
            if ch in ["+","-","*","/"]:
                b=stack.pop()
                a=stack.pop()
                if ch=="+":
                    stack.append(a+b)
                elif ch=="-":
                    stack.append(a-b)
                elif ch=="*":
                    stack.append(a*b)
                else:
                    stack.append(int(float(a)/b))
            else:
                stack.append(int(ch))
        return stack[-1]
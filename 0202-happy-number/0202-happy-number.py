class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqr(num):
            sum=0
            while num!=0:
                digit=num%10
                sum+=digit**2
                num//=10
            return sum
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=sqr(n)
        return n==1
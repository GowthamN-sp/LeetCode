class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add(num):
            total=0
            while num!=0:
                digit=num%10
                total+=digit
                num//=10
            return total
        while num>9:
            num=add(num)
        return num
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l_p=float('inf')
        h_p=0
        for price in prices:
            l_p=min(price,l_p)
            profit=price-l_p
            h_p=max(profit,h_p)
        return h_p

            
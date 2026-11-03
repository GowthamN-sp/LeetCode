class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        step=0
        for cite in range(len(citations)-1,-1,-1):
            if citations[cite]>=step+1:
                step+=1
        return step
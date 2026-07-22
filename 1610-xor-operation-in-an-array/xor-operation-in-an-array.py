class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        element=0
        for i in range(n):
            count=start+2*i
            element=element^count
        return element
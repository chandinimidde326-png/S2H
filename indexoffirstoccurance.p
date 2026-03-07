class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            s=haystack.index(needle)
            return(s)
        else:
            return(-1)

class Solution:
    def isPalindrome(self, s):
        # code here
        rev=s[::-1]
        if s==rev:
            return("true")
        else:
            return("false")

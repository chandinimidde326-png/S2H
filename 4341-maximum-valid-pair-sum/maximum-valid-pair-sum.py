class Solution(object):
    def maxValidPairSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxLeft = nums[0]
        ans = float('-inf')

        for j in range(k, len(nums)):
            maxLeft = max(maxLeft, nums[j - k])
            ans = max(ans, maxLeft + nums[j])

        return ans
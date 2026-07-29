class Solution(object):
    def findMaxAverage(self, nums, k):
        sum = 0

        for i in range(k):
            sum += nums[i]

        max_sum = sum

        for i in range(k, len(nums)):
            sum += nums[i]
            sum -= nums[i - k]
            max_sum = max(max_sum, sum)

        return max_sum / float(k)
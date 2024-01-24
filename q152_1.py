class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # return self.bottomUpQuadraticSpace(nums)
        # return self.bottomUpLinearSpace(nums)
        # return self.quadraticTime(nums)
        return self.linearTime(nums)
    
    def bottomUpQuadraticSpace(self, nums):
        # dp[i][i] = nums[i]
        # dp[i - 1][i] = max(nums[i - 1] * nums[i], nums[i], nums[i - 1])
        # dp[i][j] array to represent subarray product between i and j inclusive
        # dp[i][j] = dp[i + 1][j - 1] * nums[i] * nums[j], keep track of maximum
        if len(nums) == 1: return nums[0]
        dp = [[1 for j in range(len(nums))] for i in range(len(nums))]
        res = -math.inf

        for i in range(len(nums)):
            dp[i][i] = nums[i]
            res = max(res, dp[i][i])
        for i in range(1, len(nums)):
            dp[i - 1][i] = nums[i - 1] * nums[i]
            res = max(res, dp[i - 1][i])

        for length in range(2, len(nums)):
            for i in range(0, len(nums) - length):
                j = i + length
                dp[i][j] = dp[i + 1][j - 1] * nums[i] * nums[j]
                res = max(res, dp[i][j])
        
        return res
    
    def bottomUpLinearSpace(self, nums):
        if len(nums) == 1: return nums[0]
        dp = [1 for j in range(len(nums))]
        res = -math.inf

        for i in range(len(nums)):
            dp[i] = nums[i]
            res = max(res, dp[i])
        
        for length in range(1, len(nums)):
            for i in range(0, len(nums) - length):
                j = i + length
                dp[i] = dp[i] * nums[j]
                res = max(res, dp[i])
        
        return res
    
    def quadraticTime(self, nums):
        res = -math.inf

        for i in range(len(nums)):
            acc = 1
            for j in range(i, len(nums)):
                acc *= nums[j]
                res = max(res, acc)
        
        return res
    
    def linearTime(self, nums):
        localMin, localMax = 1, 1
        res = -math.inf

        for i in range(len(nums)):
            tmpMax = max(nums[i], localMax * nums[i], localMin * nums[i])
            localMin = min(nums[i], localMax * nums[i], localMin * nums[i])
            localMax = tmpMax

            res = max(res, localMax)
        
        return res

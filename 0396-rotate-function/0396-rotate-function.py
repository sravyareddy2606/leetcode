class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        def F(arr: List[int]) -> int:
            f = 0
            for i in range(len(arr)):
                f += (i * arr[i])
            return f
        n = len(nums)
        total_sum = sum(nums)
        dp = [F(nums)]
        for i in range(1, n):
            curr = dp[i - 1] + total_sum - n * nums[n - i]
            dp.append(curr)
        return max(dp)
# Max sum of array elements over a sliding window size k


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        if len(nums) < k:
            print("window size too big")
            return -1
        if len(nums) == k:
            return sum(nums)
        max_sum = sum(nums[0 : k - 1])
        for i in range(1, len(nums) - k + 1):
            win_sum = sum(nums[i : i + k])
            max_sum = max(max_sum, win_sum)
        return max_sum


sol = Solution()
print(sol.maxSum([80, -50, 90, 100], 2))
print(sol.maxSum([100], 1))
print(sol.maxSum([100, 200, 100], 4))

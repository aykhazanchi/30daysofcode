"""
Given an array of integers nums, there is a sliding window of size k which is moving 
from the very left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window moves right by one position.

Return the list of max elements of each sliding window.
"""


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if len(nums) < k:
            print("window size too big")
            return -1
        if len(nums) == k:
            return [max(nums)]
        max_list = []
        for i in range(len(nums) - k + 1):
            max_list.append(max(nums[i : i + k]))
        return max_list

    # With forced space complexity of O(N) (you can only see k elements at a time)
    def maxSliding(self, nums: list[int], k: int) -> list[int]:
        if len(nums) < k:
            print("window size too big")
            return -1
        if len(nums) == k:
            return [max(nums)]


sol = Solution()
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol.maxSlidingWindow([100], 1))
print(sol.maxSlidingWindow([100, 200, 100], 2))

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

https://leetcode.com/problems/missing-number/
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        # go from 0 to len(nums) + 1
        # so for [0,1] i would go from 0 to 2
        for i in range(len(nums) + 1):
            # if i == len(nums) means we've come to the end and nothing is missing so far
            if i == len(nums) or nums[i] != i:
                # because list goes from [0 - n], nums[i] should always equal i
                # if not, i is our missing number
                return i


sol = Solution()
print(sol.missingNumber([3, 2, 1]))
print(sol.missingNumber([0, 1]))
print(sol.missingNumber([3, 0, 1]))
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

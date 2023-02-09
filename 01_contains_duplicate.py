# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, num in enumerate(nums):
            print(num)
            if i<len(nums)-1 and num == nums[i+1]:
                return True
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         data = set()
#         for n in nums:
#             if n in data:
#                 return True
#             data.add(n)
#         return False


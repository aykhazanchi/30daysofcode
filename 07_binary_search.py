'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write 
a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/binary-search/description/
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min = 0
        max = len(nums) - 1
        while True:
            if max < min:
                return -1
            mid = int((max + min) / 2)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                min = mid + 1
            if target < nums[mid]:
                max = mid - 1
            

sol = Solution()
sol.search([-1,0,3,5,9,12], 9)
sol.search([-1,0,3,5,9,12], 2)
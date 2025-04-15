"""
Problem: Two Sum
Given: An array of integers nums and an integer target.
Goal: Return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  # because nums[0] + nums[1] = 2 + 7 = 9

"""

"""
solution 1__BRUTE_FORCE (Idea: Try every possible pair.)
"""

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

"""
solution 2__OPTIMIZED (Idea: USING HASHMAPS.) with time complexity o(n^2)
"""

def twoSum(nums, target):
    seen = {}  # number: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

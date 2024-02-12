from typing import List
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

#Brute force solution
def contains_duplicates(nums: List[int]) -> bool:
    #compare each element against each other elment in the array
    n = len(nums)
    for i in range(n):
        for j in nums[i+1:]:
            if nums[i] == nums[j]:
                return True
    return False
# tests

# Optimized solution
def contains_duplicates(nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

nums = [1,2,3,1]
print(contains_duplicates(nums))
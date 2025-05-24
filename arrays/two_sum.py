"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Approach:
- Use a hashmap (dictionary) to store the value-to-index mapping.
- For each element, calculate the complement (target - current number).
- If the complement exists in the map, return the pair of indices.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number -> index
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            # Store current number and its index
            prevMap[n] = i

# Example usage (for testing):
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

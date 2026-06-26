"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Approach: Use a hash map to store visited numbers and their indices.
Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))

"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Approach: Count character frequencies in both strings and compare.
Time Complexity: O(n)
Space Complexity: O(1) for fixed alphabet / O(n) generally
"""


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] < 0:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram('anagram', 'nagaram'))

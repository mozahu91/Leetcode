"""
242. Valid Anagram
Easy

1054

127

Add to List

Share
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in t:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1
        
        for k in count:
            if count[k] != 0:
                return False
        
        return True

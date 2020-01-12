"""
249. Group Shifted Strings
Medium

342

58

Add to List

Share
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

import collections
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strings:
            k = []
            for i in range(len(s)-1):
                k.append(str((ord(s[i+1])-ord(s[i]))%26))
            k = ''.join(k)
            d[k].append(s)
        return list(d.values())
                

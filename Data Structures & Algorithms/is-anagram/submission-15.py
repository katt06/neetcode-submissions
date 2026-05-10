class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the strings
        # nested loop, comparing all characters
        # if the same, then return true

        return sorted(s) == sorted(t)
        
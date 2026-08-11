class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        mapMeow = {}

        for r in range(len(s)):
            if s[r] in mapMeow:
                l = max(mapMeow[s[r]] + 1, l)

            mapMeow[s[r]] = r
            result = max(result, r-l + 1)

        return result
        


            
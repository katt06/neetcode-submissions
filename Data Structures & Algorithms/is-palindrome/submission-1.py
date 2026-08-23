class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            #move left and right until they hit a alphanumeral

            while left < right and not s[left].isalnum():
                left += 1
                #exit once we hit a IS self.alphaNum
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True

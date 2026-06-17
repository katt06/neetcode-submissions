class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        copy = []
        for letter in s:
            if letter.isalnum():
                copy.append(letter.lower())

        #convert back to string
        copy = ''.join(copy)

        return copy == copy[::-1]



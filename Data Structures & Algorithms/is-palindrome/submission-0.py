class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if char.isdigit() or char.isalpha():
                result += char.lower()
        return result == result[::-1]
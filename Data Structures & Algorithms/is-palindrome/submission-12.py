class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev_str = ""
        for char in s:
            if char.isalnum():
                rev_str += char.lower()
        return rev_str == rev_str[::-1]
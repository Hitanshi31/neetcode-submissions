class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = [c.lower() for c in s if c.isalnum()] 
        return clean_str == clean_str[::-1]
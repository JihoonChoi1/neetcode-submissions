class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, h) -> bool:
            while l < h:
                if s[l] != s[h]:
                    return False
                l += 1
                h -= 1
            return True
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return isPalindrome(low + 1, high) or isPalindrome(low, high - 1)
            else:
                low += 1
                high -= 1
        return True
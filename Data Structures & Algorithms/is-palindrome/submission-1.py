class Solution:
    def isPalindrome(self, s: str) -> bool:

        clen = ""

        for ch in s:
            if ch.isalnum():
                clen += ch.lower()

        return clen == clen[::-1]
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            cur = ""

            for j in range(i , len(s)):
                if s[j] in cur:
                    break

                cur += s[j]

                max_len = max(max_len , len(cur))

        return max_len
                
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 and s == s[::-1]:
            return s

        longest = ''
        for i in range(len(s) - 1):
            longest = max(longest, find(i, i + 1), find(i, i + 2), key=len)

        return longest
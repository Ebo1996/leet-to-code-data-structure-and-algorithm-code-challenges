class Solution(object):
    def countPalindromicSubsequence(self, s):
        first = {}
        last = {}

        # record first and last occurrence of each character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        ans = 0

        # consider each letter as the outer characters of palindrome
        for ch in first:
            if first[ch] < last[ch]:
                # unique middle chars between them
                mid = set(s[first[ch] + 1 : last[ch]])
                ans += len(mid)

        return ans

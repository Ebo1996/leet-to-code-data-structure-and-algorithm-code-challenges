class Solution(object):
    def isMatch(self, s, p):
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # pattern finished → must also finish string
            if j == len(p):
                return i == len(s)
            
            # first character match?
            first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")
            
            # check if next pattern char is "*"
            if j + 1 < len(p) and p[j + 1] == "*":
                # two choices:
                # 1. skip "x*" entirely
                # 2. if first_match, consume 1 char from s
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                ans = first_match and dp(i + 1, j + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)

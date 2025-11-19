class Solution(object):
    def countAndSay(self, n):
        s = "1"
        for _ in range(1, n):
            i = 0
            nxt = []
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                nxt.append(str(j - i))
                nxt.append(s[i])
                i = j
            s = "".join(nxt)
        return s

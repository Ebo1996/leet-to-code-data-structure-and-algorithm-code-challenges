class Solution(object):
    def minimumDeletions(self, word, k):
        from collections import Counter
        freq = list(Counter(word).values())
        maxf = max(freq)
        ans = float('inf')

        for fmax in range(maxf + 1):
            fmin = max(0, fmax - k)
            deletions = 0

            for f in freq:
                if f > fmax:
                    deletions += f - fmax
                elif f < fmin:
                    deletions += f

            ans = min(ans, deletions)

        return ans

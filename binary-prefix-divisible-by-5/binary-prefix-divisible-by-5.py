class Solution(object):
    def prefixesDivBy5(self, nums):
        res = []
        prefix = 0
        
        for bit in nums:
            prefix = (prefix * 2 + bit) % 5
            res.append(prefix == 0)
        
        return res

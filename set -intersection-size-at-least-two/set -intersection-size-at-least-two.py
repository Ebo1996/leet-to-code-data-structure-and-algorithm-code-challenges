class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # Sort by end ASC, and if same end, by start DESC
        intervals.sort(key=lambda x: (x[1], -x[0]))

        res = []
        a = b = -1  

        for s, e in intervals:
            
            if s > b:
                res.append(e - 1)
                res.append(e)
                a, b = e - 1, e

           
            elif s > a:
                res.append(e)
                a, b = b, e

            
        return len(res)

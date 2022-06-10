"""
https://leetcode.com/problems/teemo-attacking/
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        n = len(timeSeries)
        
        for i in range(1, n):
            i1 = timeSeries[i - 1]
            i2 = timeSeries[i]
            
            # if the gap between timeseries is not at least the length of duration,
            #   duration needs to be shorted
            count += min(duration, i2 - i1)
            
        # last timeseries will always have the full duration
        count += duration
        
        return count

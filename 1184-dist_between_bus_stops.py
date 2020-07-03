"""
https://leetcode.com/problems/distance-between-bus-stops/submissions/

Strat: calculate the distance when going clockwise and then counterclockwise. Then
    return the smaller of the two.

Stats: O(n) time, O(1) space
    Runtime: 52 ms, faster than 9.41% of Python online submissions for Distance Between Bus Stops.
    Memory Usage: 13.2 MB, less than 67.06% of Python online submissions for Distance Between Bus Stops.

Awesome solution: https://leetcode.com/problems/distance-between-bus-stops/discuss/481987/Python-O(-n-)-sol-by-shortest-path.-90%2B-With-explanation
"""
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        #ensure start is less than destination
        if start > destination:
            start, destination = destination, start
            
        clockwise = 0
        for i in range(start, destination):
            clockwise += distance[i]
            
        counter_clockwise = 0
        i = destination
        while i != start:
            counter_clockwise += distance[i % len(distance)]
            i = (i + 1) % len(distance)
            
        return min(clockwise, counter_clockwise)

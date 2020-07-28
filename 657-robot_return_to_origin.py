"""
https://leetcode.com/problems/robot-return-to-origin/solution/

Strat:
    In essence, the L and R vectors have to cancel out for us to have no
    movement in the x-axis. Same logic applies to the U and D vectors.
    Count the number of vectors and return if they cancel out.
    
Stats: O(n) time, O(1) space
"""
class Solution(object):
    """
    Runtime: 92 ms, faster than 44.83% of Python online submissions for Robot Return to Origin.
    Memory Usage: 13 MB, less than 34.48% of Python online submissions for Robot Return to Origin.
    """
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x_axis, y_axis = 0, 0
        for move in moves:
            if move == "U":
                y_axis += 1
            elif move == "D":
                y_axis -= 1
            elif move == "R":
                x_axis += 1
            elif move == "L":
                x_axis -= 1
        
        return x_axis == y_axis == 0
    
    
    """
    Runtime: 28 ms, faster than 89.66% of Python online submissions for Robot Return to Origin.
    Memory Usage: 13 MB, less than 31.03% of Python online submissions for Robot Return to Origin.
    """
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("D") == moves.count("U") and moves.count("L") == moves.count("R")

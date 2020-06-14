"""
https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/submissions/

Runtime: 24 ms, faster than 81.31% of Python online submissions for Number of Students Doing Homework at a Given Time.
Memory Usage: 12.7 MB, less than 62.91% of Python online submissions for Number of Students Doing Homework at a Given Time.     
"""
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        result = 0
        for start, end in zip(startTime, endTime):
            print(start, end)
            if start <= queryTime <= end:
                result += 1 
        
        return result
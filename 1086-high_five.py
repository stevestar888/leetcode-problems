"""
https://leetcode.com/problems/high-five/
"""
class Solution(object):
    """
    Strat:
        One easy way to get all the student IDs bunched together is by sorting.
        If we use the built in sort on the [id, score] array, the id attribute
        is sorted on first, followed by the socre attribute. Since we want the 
        top 5 scores, it's actually easier to sort reversed, because you can 
        take the first 5 scores of any given id, and you know those are the top
        5.
    
    Stats:
        O(n lg n), where n = len(items) or # of [id, score] pairs
        We have to sort
    """
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        #constants
        GRADE_COUNT = 5
        ID_INDEX = 0
        SCORE_INDEX = 1
        
        #sort all items
        #id desc., grades desc.
        items = sorted(items, reverse=True)
        
        result = []
        
        ptr = 0
        curr_id = -1
        grade_sum = 0
        grade_count = 0
        while ptr < len(items):
            id_num = items[ptr][ID_INDEX]
            score = items[ptr][SCORE_INDEX]
            
            #found new student
            if curr_id != id_num:
                curr_id = id_num
                grade_sum = 0
                grade_count = 0
            
            if grade_count <= GRADE_COUNT: #take top GRADE_COUNT (5) scores
                grade_sum += score
                grade_count += 1
                
                if grade_count == GRADE_COUNT:
                    pair = [curr_id, grade_sum // GRADE_COUNT]
                    result.append(pair)
            
            ptr += 1
        
        #reverse the student IDs, so we get asc order
        return result[::-1]

    
"""
https://leetcode.com/problems/high-five/discuss/630377/Python-object-oriented-solution-O(n)-runtime

R
"""
from collections import defaultdict
import heapq as hq


class TopScoresBuffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = []
    
    def get_avg(self):
        return sum(self.buffer) // len(self.buffer)
    
    def report(self, grade):
        if len(self.buffer) < self.max_size:
            hq.heappush(self.buffer, grade)
        elif grade > self.buffer[0]:
            hq.heapreplace(self.buffer, grade)
            

class Solution:
    def highFive(self, items):
        top_scores = defaultdict(lambda : TopScoresBuffer(5))
        student_ids_queue = []
        student_ids_seen = set()
        
        for student_id, grade in items:
            top_scores[student_id].report(grade)
            if student_id not in student_ids_seen:
                student_ids_queue.append(student_id)
                student_ids_seen.add(student_id)
                
        return [[sid, top_scores[sid].get_avg()] for sid in student_ids_queue]
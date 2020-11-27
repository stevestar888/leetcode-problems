"""
https://leetcode.com/problems/employee-importance/submissions/

Strat:
    Use a dictionary to preprocess, then do BFS.
    
Stats: O(n) / linear time, O(n) / linear space 
    Runtime: 148 ms, faster than 92.11% of Python online submissions for Employee Importance.
    Memory Usage: 14.5 MB, less than 98.33% of Python online submissions for Employee Importance.

# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        #preprocess list of employees
        ees = {}
        
        for ee in employees:
            id_num = ee.id

            ees[id_num] = ee
        
        #begin BFS
        total_importance = 0
        ees_to_add = [id]
        
        while ees_to_add:
            ee_id = ees_to_add.pop()
            
            importance_val = ees[ee_id].importance
            subordinates = ees[ee_id].subordinates
            
            total_importance += importance_val
            ees_to_add.extend(subordinates) #add all subordinates
            
        return total_importance

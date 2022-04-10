"""
https://leetcode.com/problems/maximum-units-on-a-truck/

Strat:
    Sort & greedy
    
Stats: O(n lg n) time, O(n) / linear space 
    Runtime: 128 ms, faster than 79.47% of Python online submissions for Maximum Units on a Truck.
    Memory Usage: 13.9 MB, less than 86.31% of Python online submissions for Maximum Units on a Truck.
"""
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes = sorted(boxTypes, key=lambda x : x[1], reverse=True)
        
        units_fitted = 0
        space_left = truckSize
        for box in boxTypes:
            num_of_boxes = box[0]
            num_of_units_in_box = box[1]
            
            if space_left > num_of_boxes:
                units_fitted += num_of_boxes * num_of_units_in_box
                space_left -= num_of_boxes
            else:
                units_fitted += space_left * num_of_units_in_box
                break
                
        return units_fitted

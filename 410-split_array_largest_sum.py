"""
https://leetcode.com/problems/split-array-largest-sum/submissions/

Strat:
    Use Binary Search. While nums isn't sorted and we can't do binary search on that,
    we can do binary search on the possibilies of the output (this is very similar 
    logic to finding the root of a number via binary search). The first observation is
    that max(nums) ≤ output ≤ sum(nums)--the min weight you'd ever need to take is the 
    biggest num, and the max weight you'd ever need to take is the whole array. So 
    in the binary serach, if a particular output works, search the left half; else, 
    search the right half.
        
Stats:
    Runtime: 40 ms, faster than 39.27% of Python online submissions for Split Array Largest Sum.
    Memory Usage: 12.8 MB, less than 66.10% of Python online submissions for Split Array Largest Sum.
    
Great solution, clear & documented: https://leetcode.com/problems/split-array-largest-sum/discuss/373306/Python3-BinarySearch-Accepted-and-Well-Documented-Solution
"""
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """     
        def can_contain_weight(weight_per_section):
            # num of splits = num of sections + 1
            sections_left = m - 1
            weight_left = weight_per_section
            
            for num in nums:
                #see if we can fit num in weight_left
                #if yes - subtract from weight_left
                #if no  - use a "split" & reset weight_left
                if weight_left - num < 0:
                    if sections_left > 0: #check if we have another section to use
                        sections_left -= 1
                        weight_left = weight_per_section #reset weight
                    else:
                        #if we're out of splits, we cannot contain
                        return False
                    
                weight_left -= num
            
            return True
        #-------------------end helper method-------------------
        
        if m == 1:
            return sum(nums)
        
        lo, hi = max(nums), sum(nums)
        # result = -1
        while lo < hi:
            mid = lo + (hi - lo >> 1) #trendy
            
            if can_contain_weight(mid):
                #try going lower
                # result = mid
                hi = mid
            else:
                #go higher
                lo = mid + 1
        
        return lo

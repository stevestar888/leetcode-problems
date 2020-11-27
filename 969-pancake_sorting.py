"""
https://leetcode.com/problems/pancake-sorting/

(Hmm code doesn't 100% work, but logic should be correct)

Strat: 
    #_of_elems_already_in_right_place = 0
    Find max of arr
    Swap max to beginning [call flip(index_of_max)]
    Swap max to right position [call flip(arr_len - #_of_elems_already_in_right_place)]
    #_of_elems_already_in_right_place += 1
    Repeat
    
Good solution, but uses extra DS:
    https://leetcode.com/problems/pancake-sorting/discuss/274921/Python-Detailed-Explanation-for-This-Problem

Some magic:
    https://leetcode.com/problems/pancake-sorting/discuss/494417/Dew-It-or-True-O(n)-or-Explained-with-Diagrams
"""
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def flip(k):
            arr[:] = arr[:k][::-1] + arr[k:]
            # for i in range((k + 1) // 2):
            #     tmp = arr[i]
            #     arr[i] = arr[k - i]
            #     arr[k - i] = tmp
        
        def find_max_num_index(top_index):
            max = float('inf')
            idx = -1
            for i in range(top_index):
                if arr[i] > max:
                    max = arr[i]
                    idx = i
            return idx

        for i in range(len(arr), 0, -1):
            #look for the big number from arr[0:i]
            biggest = find_max_num_index(i)
            
            #move the biggest to the front
            flip(biggest)
            print(arr)
            
            #move the biggest to the i-th position, which is the right spot
            flip(i)
            
        return arr
    
    """
    Interesting idea, similar to bubble sort
    #TODO
    """
    def pancakeSort(self, arr):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        print(arr)
        def flip(k):
            arr[:] = arr[:k][::-1] + arr[k:]

        i = 0
        while i < len(arr) and arr[i] < arr[i + 1]:
            i += 1
        
        if i == len(arr) - 1:
            return arr
        else:
            k = i
            return self.pancakeSort(arr[:k][::-1] + arr[k:])
    

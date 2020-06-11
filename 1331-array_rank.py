#TODO
"""
https://leetcode.com/problems/rank-transform-of-an-array/
"""
def arrayRankTransform(self, arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    
    results = arr[:]

    # sort results
    sorted_arr = sorted(arr[:])

    rank = 0
    prev_elem = None
    for i in range(len(arr)):
        elem = sorted_arr[i]

        if elem != prev_elem:
            rank += 1

        elem_index = arr.index(elem)

        print("element", elem)
        print("index", elem_index)
        print("rank", rank)
        print("")

        results[elem_index] = rank
        arr[elem_index] = None
        prev_elem = elem
        
        return(results)
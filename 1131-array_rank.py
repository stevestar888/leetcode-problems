from heapq import heapify, heappush, heappop 

def arrayRankTransform(self, arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    
    result = arr[:]
    
    # Creating empty heap 
    heap = [] 
    heapify(heap) 

    # Adding items to the heap using heappush function 
    for elem in arr:
        heappush(heap, elem) 
    
    rank = 0
    prev_elem = None
    for _ in range(len(heap)): #for every elem in heap
        element = heappop(heap) 
        
        if element != prev_elem:
            rank += 1
            
        #find the index of element
        ele_index = arr.index(element)
        
        print("element", element)
        print("index", ele_index)
        print("rank", rank)
        print("result", result)
        print("")
        
        result[ele_index] = rank
        arr[ele_index] = None
        prev_elem = element
    
    return(result)

def arrayRankTransform(self, arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    
    result = arr[:]
    
    # sort results
    result = sorted(result)
    
    rank = 0
    prev_elem = None
    for i in range(len(result)):
        elem = result[i]
        
        if elem != prev_elem:
            rank += 1
            
        elem_index = arr.index(elem)
        
        # print("element", elem)
        # print("index", elem_index)
        # print("rank", rank)
        # print("result", result)
        # print("")
        
        result[elem_index] = rank
        arr[elem_index] = None
        prev_elem = elem
    
    return(result)
        

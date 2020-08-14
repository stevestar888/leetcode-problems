"""
Fri, Aug 14, 2020, 8:04 AM



input:  arr = [4, 6, 10, 15, 16],  lim = 21
                  ^      ^
                  6+    15   =   21
                  
output: [3, 1] # since these are the indices of the
               # weights 6 and 15 whose sum equals to 21


arr = [4, 6, 10, 15, 16] --> O(n^2)


arr = [4, 6, 10, 15, 16]
map = {4: 0, 6: 1, 10: 2, ...}

xx 1. preprocess' O(n)
2. see if limit - arr[i] != what we get from map O(n)
xx 3. check if i > j O(1)

arr = [4, 6, 10, 15, 16]
       ^
map = {4: 0, }

1. traverse through arr --> O(n) (one pass)
2. look if we have the complement in the map
3. if yes: return
   if no: put in map
"""
def get_indices_of_item_wights(arr, limit):
  complements = {}
  
  for i, val in enumerate(arr):
    complement = limit - val
    
    if complements.get(complement, -1) > -1:
      #i is guranteed to be bigger than complement's index
      return [i, complements.get(complement)]
    else:
      #put in dict
      complements[val] = i

   #if we didn't find complement
  return []
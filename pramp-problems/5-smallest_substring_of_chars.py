"""
Thu, Aug 13, 2020, 4:04 PM
"""

"""
The another guy's approach

import collections
def get_shortest_unique_substring(arr, word):
  
  arrdict = collections.defaultdict(int)
  
  windowdict = collections.defaultdict(int)
  found_so_far = 0
  low = 0
  curr = 0
  ans = ""
  
  ans_len = float('inf')
  for ch in arr:
    arrdict[ch] += 1
  while(curr < len(word)):
    if word[curr] not in arrdict:
      continue
    else:
      windowdict[word[curr] ] += 1
      if windowdict[word[curr] ] == arr[word[curr]]:
        found_so_far+=1
      if found_so_far == len(arrdict):
        window_len = curr - low+1
        if window_len < ans_len:
          ans = word[low:curr+1]
          ans_len = window_len
        windowdict[word[low]]-=1
        if windowdict[word[low]] < arrdict[word[low]]:
          found_so_far-=1          
        low += 1
        
      while low <=curr and windowdict[word[low]] > arrdict[word[low]]:
        windowdict[word[low]]-=1
        low+=1
    curr += 1
  return ans

print(get_shortest_unique_substring(['x','y','z'], "xyyzyzyx"))
        
      

"""
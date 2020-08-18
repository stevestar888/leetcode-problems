"""
https://www.pramp.com/challenge/jKoA5GAVy9Sr9jGBjzN4

find the n-th root of x

n -> positive integer
x -> positive (could be a float)

must be within 0.001 of the actual root

input:  x = 7, n = 3
output: 1.913



output (1 + 0.901) ** 3 = 7 --> O(n) n=0.001

Binary Search -> O(lg n)

input:  x = 9, n = 2
output: 3

start = 0 .... end = 9
mid = 4.5 ^ 2 = 17 > 9 

start = 0 .... end = 4.5 (mid)
mid = 2.25 ^ 2 = 4.625 < 9

1. start & end pointer
2. calculate what mid is and take it to the power of n
3. compare to x (final goal) ... check if we're within precision
4. search either the left or right half
"""
def root(x, n):
  start, end = 0.0, x #use 0.0 to ensure float
  
  while start <= end:
    mid = start + (end - start) / 2
    
    product = mid ** n
    if x - 0.001 < product < x + 0.001:
      return mid

    #check if we search left or right
    if product > x: # num too big, search left
      end = mid
    else: #num too small, search right
      start = mid
      
  return -1
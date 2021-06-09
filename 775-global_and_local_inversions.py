"""
https://leetcode.com/problems/global-and-local-inversions/

TODO: global inversions not working & there's a better way to do...
"""
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def localCount():
            inv_count = 0
            for i in range(len(A) - 1): #stop 1 short of end so we can check A[i + 1]
                if A[i] > A[i + 1]:
                    inv_count += 1
            return inv_count

        # modification of MergeSort
        def globalCount(A):
            #basecase
            if len(A) == 1:
                return 0
            
            #find left, right, and straddle
            halfway = len(A) // 2
            left = A[:halfway]
            right = A[halfway:]

            straddle_count = 0

            for l in left:
                for r in right:
                    if l > r:
                        straddle_count += 1

            return globalCount(left) + globalCount(right) + straddle_count

        # return localCount()
        return globalCount(A) == localCount()


A = [1, 2, 3, 4]
A = [12, 3, 4, 9, 8, 22]
# A = [1,0,2] #true
# A = [1,2,0] #false

obj = Solution.isIdealPermutation(None, A)
print(obj)

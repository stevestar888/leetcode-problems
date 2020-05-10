"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Strat:
    For a given kid, we just have to see if their candies + extraCandies is the most (or equal to)
    all the other children's. The trick: the kid with the most candy (before extras are added)
    will always be the same.

    Therefore, find the max_candies and iterate through candies to see if kid + extraCandies ≥ max_candies.

Speed: O(n) - 2 pass throughs, both O(n)
    Runtime: 8 ms, faster than 100% of Python online submissions for Kids With the Greatest Number of Candies.
    Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Kids With the Greatest Number of Candies.

"""     

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        #find the max candies
        max_candy = -1
        for candy in candies:
            if candy > max_candy:
                max_candy = candy
        max_candy = max(candies)
        
        #see if a given kid will have the most, after they receive the extra candy
        ans = []
        for candy in candies:
            ans.append(candy + extraCandies >= max_candy)
        return ans


    # one liner haha
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return [(candy + extraCandies >= max(candies)) for candy in candies]
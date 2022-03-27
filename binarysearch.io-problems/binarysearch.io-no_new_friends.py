"""
https://binarysearch.io/question/231

You are given n people represented as an integer from 0 to n - 1, and a list of friends tuples, where person friends[i][0] and person friends[i][1] are friends.

Return whether everyone has at least one friend.
"""
class Solution:
    def solve(self, n, friends):
        friend_pairs = {}
        
        for pair in friends:
            p1 = pair[0]
            p2 = pair[1]
            
            friend_pairs[p1] = friend_pairs.get(p1, 0) + 1
            friend_pairs[p2] = friend_pairs.get(p2, 0) + 1
        
        return all(people > 0 for people in friend_pairs.values()) and len(friend_pairs.keys()) == n
"""
Jul 18, 2020 - solved sucessful during interview
https://www.pramp.com/question/15oxrQx6LjtQj9JK9XqA

Given tree (not necessarily binary) (each child has a cost), 
find the minimium cost path
  cheapest: 0 + 3 + 2 + 1 + 1 = 7
         or 6 + 1 = 7

Strat: 
  Use DFS & get the min of all children on each level.

Stats: O(n) time, O(n) space
  Note on space: worst case is O(n), but avg: [height of tree]
"""


def get_cheapest_cost(node):
    # base case
    if node == None:
        return 0

    # recursive case
    cheapest = float('inf')
    for child in node.children:
        cost = get_cheapest_cost(child)
        cheapest = min(cheapest, cost)

    return node.cost + cheapest


class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

# root = Node(0)
# root.children = [Node(1), Node(3), Node(42)]
# print(get_cheapest_cost(root))

"""
https://leetcode.com/problems/two-city-scheduling/submissions/

Stats: 
    Runtime: 36 ms, faster than 13.52% of Python online submissions for Two City Scheduling.
    Memory Usage: 12.7 MB, less than 76.69% of Python online submissions for Two City Scheduling. 
"""


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prices = []  # storing tupples: (index: price difference)

        for i, pair in enumerate(costs):
            prices.append((abs(costs[i][1] - costs[i][0]), i))

        city1_max, city2_max = len(costs) / 2, len(costs) / 2
        total_cost = 0
        for price in sorted(prices, reverse=True):  # biggest on top
            i = price[1]  # index

            # find costs
            flight1 = costs[i][0]
            flight2 = costs[i][1]

            # choose between flight1 and flight2
            if city1_max and city2_max:
                # have the freedom to choose either flight1 or flight2
                if flight2 > flight1:  # flight 1 is cheaper
                    city1_max -= 1
                    total_cost += flight1
                else:  # flight 2 is cheaper
                    city2_max -= 1
                    total_cost += flight2
            elif city1_max:
                # flight2 is full, must take flight 1
                city1_max -= 1
                total_cost += flight1

            else:
                # flight1 is full, must take flight 2
                city2_max -= 1
                total_cost += flight2

        return total_cost

    # even better solution (not mine)
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(costs, key=lambda x: abs(x[0]-x[1]), reverse=True)
        max_a = max_b = len(costs) // 2
        min_cost = 0
        for cost_a, cost_b in costs:
            if cost_a < cost_b:
                if max_a > 0:
                    min_cost += cost_a
                    max_a -= 1
                else:
                    min_cost += cost_b
                    max_b -= 1
            else:
                if max_b > 0:
                    min_cost += cost_b
                    max_b -= 1
                else:
                    min_cost += cost_a
                    max_a -= 1
        return min_cost

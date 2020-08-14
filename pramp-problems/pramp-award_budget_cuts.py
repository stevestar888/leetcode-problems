"""
https://www.pramp.com/challenge/r1Kw0vwG6OhK9AEGAyWV

Given an array grantsArray of the original grants and the reduced budget newBudget, 
write a function findGrantsCap that finds in the most efficient manner a cap such that 
the least number of recipients is impacted and that the new budget constraint is met.

grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190 (total amount we can spend)
cap (output) = 47 --> [2, 47, 47, 47, 47]

Thinking process: 
cap = 2
2 + 50(4) = 202 > 190
188 / 4 = 47

1. sort (no need for indices)
2. try to fund as many grants as possible
"""


def find_grants_cap(grantsArray, newBudget):
    length = len(grantsArray)
    # sort grants
    grants = sorted(grantsArray)

    for i, grant_cost in enumerate(grants):
        # check if we can fund the study
        cost = (length - i) * grant_cost

        if cost < newBudget:
            # funded study at i
            newBudget -= grant_cost
        else:
            # cannot fund the rest of the studies
            return float(newBudget) / float((length - i))

    # in case we're able to fund ALL studies, this is the most expensive
    return grants[-1]

"""
https://leetcode.com/problems/fizz-buzz/

The Tom Scott solution!
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            
            if output == "":
                output = str(i)
            
            res.append(output)
        
        return res


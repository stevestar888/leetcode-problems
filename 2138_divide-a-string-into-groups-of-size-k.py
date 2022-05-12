"""
https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
"""
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        counter = 0
        string_builder = ""
        output = []
        
        for letter in s:
            string_builder += letter
            counter += 1
            
            if counter == k:
                output.append(string_builder)
                counter = 0
                string_builder = ""
                
        if counter != 0:
            spaces_left = k - len(string_builder)
            string_builder += fill * spaces_left
            output.append(string_builder)
            
        return output
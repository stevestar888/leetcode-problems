"""
https://leetcode.com/problems/logger-rate-limiter/

Strat:
    Use a hashmap to store the previous timestamp a message was sent.
    We can index into that hashmap in constant time, and update accordingly.
    
Stats: O(1), O(n) / linear space -- constant dict lookup + log can get up to n size
    Runtime: 124 ms, faster than 94.08% of Python online submissions for Logger Rate Limiter.
    Memory Usage: 20.1 MB, less than 48.90% of Python online submissions for Logger Rate Limiter.
"""
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.BREAK_INTERVAL = 10
        self.log = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.log: #first time seen
            self.log[message] = timestamp
            return True
        
        #message seen before; see if it has been called in past BREAK_INTERVAL
        if self.log.get(message) + 10 <= timestamp:
            self.log[message] = timestamp
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
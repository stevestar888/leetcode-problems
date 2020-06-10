"""
https://leetcode.com/problems/word-search/submissions/

Runtime:
    Runtime: 456 ms, faster than 20.23% of Python online submissions for Word Search.
    Memory Usage: 17.1 MB, less than 42.76% of Python online submissions for Word Search.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if self.helper(i, j, word, set(), board):
                    return True
        return False
        
        
    def helper(self, i, j, word, visited, board):
        #found the whole word
        if word == "":
            return True
        
        #check if i, j is valid
        tmp = word[0]
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
            word = word[1:] 
        else: #index out of bounds or invalid letter
            return False
        
        board[i][j] = " " #marking we've seen the square
        
        #send 4 recursive calls: up down left right
        found = self.helper(i, j + 1, word, visited, board) or \
            self.helper(i, j - 1, word, visited, board) or \
            self.helper(i + 1, j, word, visited, board) or \
            self.helper(i - 1, j, word, visited, board)
        
        if found:
            return True
        else:
            board[i][j] = tmp #restore the board
            return False
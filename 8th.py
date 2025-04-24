from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize a 3x3 board with empty spaces
        board = [[' ' for _ in range(3)] for _ in range(3)]
        
        # Go through each move
        for i, (row, col) in enumerate(moves):
            # Determine current player: Player A (X) or Player B (O)
            player = 'X' if i % 2 == 0 else 'O'
            board[row][col] = player
            
            # Check if the current player has won after this move
            if self.check_winner(board, player):
                return "A" if player == 'X' else "B"
        
        # If all moves are played and there's no winner, check if it's a draw
        if len(moves) == 9:
            return "Draw"
        
        # If there are still empty spaces, the game is pending
        return "Pending"

    def check_winner(self, board, player):
        # Check rows and columns for a win
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # Check row
                return True
            if all(board[j][i] == player for j in range(3)):  # Check column
                return True
        
        # Check diagonals for a win
        if all(board[i][i] == player for i in range(3)):  # Main diagonal
            return True
        if all(board[i][2 - i] == player for i in range(3)):  # Anti diagonal
            return True
        
        return False

# Example usage:
sol = Solution()
print(sol.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))  # Output: "A"
print(sol.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))  # Output: "B"
print(sol.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]))  # Output: "Draw"

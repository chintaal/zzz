class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]

    def is_winner(self, p):
        for i in range(3):
            if all(self.board[i][j] == p for j in range(3)): return True
            if all(self.board[j][i] == p for j in range(3)): return True
        if all(self.board[i][i] == p for i in range(3)): return True
        if all(self.board[i][2-i] == p for i in range(3)): return True
        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def minimax(self, player):
        if self.is_winner('X'): return 1
        if self.is_winner('O'): return -1
        if self.is_draw(): return 0

        scores = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = player
                    score = self.minimax('O' if player == 'X' else 'X')
                    self.board[i][j] = ' '
                    scores.append(score)

        return max(scores) if player == 'X' else min(scores)

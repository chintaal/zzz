print("="*50)
print("Tic-Tac-Toe with Minimax AI")
print("="*50)
print("\nPositions are numbered 1-9:")
print(" 1 | 2 | 3")
print("-----------")
print(" 4 | 5 | 6")
print("-----------")
print(" 7 | 8 | 9")
print("="*50)

class TicTacToe:
    def __init__(self):
        self.board = [[' ']*3 for _ in range(3)]

    def display(self):
        print("\n" + "="*11)
        for i, row in enumerate(self.board):
            print(f" {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("-----------")
        print("="*11)

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
    
    def get_best_move(self, player):
        best_score = -float('inf') if player == 'X' else float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = player
                    score = self.minimax('O' if player == 'X' else 'X')
                    self.board[i][j] = ' '
                    if (player == 'X' and score > best_score) or (player == 'O' and score < best_score):
                        best_score = score
                        best_move = (i, j)
        return best_move

# Interactive game
game = TicTacToe()
human = input("\nChoose your symbol (X/O): ").upper()
while human not in ['X', 'O']:
    human = input("Please choose X or O: ").upper()

ai = 'O' if human == 'X' else 'X'
print(f"\nYou are {human}, AI is {ai}")
current = 'X'

if ai == 'X':
    print("\n→ AI goes first")
    move = game.get_best_move(ai)
    game.board[move[0]][move[1]] = ai
    current = 'O'

while True:
    game.display()
    
    if game.is_winner(human):
        print("\n🎉 You win!")
        break
    elif game.is_winner(ai):
        print("\n💻 AI wins!")
        break
    elif game.is_draw():
        print("\n🤝 It's a draw!")
        break
    
    if current == human:
        while True:
            try:
                pos = int(input("\nYour move (1-9): "))
                if 1 <= pos <= 9:
                    row, col = (pos-1)//3, (pos-1)%3
                    if game.board[row][col] == ' ':
                        game.board[row][col] = human
                        break
                    print("Position already taken!")
                else:
                    print("Enter a number between 1 and 9!")
            except ValueError:
                print("Please enter a number!")
        current = ai
    else:
        print("\n→ AI is thinking...")
        move = game.get_best_move(ai)
        game.board[move[0]][move[1]] = ai
        print(f"✓ AI plays position {move[0]*3 + move[1] + 1}")
        current = human

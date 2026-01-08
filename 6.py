print("="*50)
print("Race to 20 Game - Minimax Algorithm")
print("="*50)
print("\nRules: Players take turns adding 1, 2, or 3 to the total.")
print("Goal: Be the player who reaches exactly 20!")
print("="*50)

def minimax(total, turn, alpha, beta):
    if total == 20:
        return 0
    if total > 20:
        return -1 if turn else 1

    if turn:
        best = -float('inf')
        for i in range(1, 4):
            best = max(best, minimax(total+i, False, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(1, 4):
            best = min(best, minimax(total+i, True, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def get_best_move(total):
    best_move = 1
    best_score = -float('inf')
    for move in range(1, 4):
        if total + move <= 20:
            score = minimax(total + move, False, -float('inf'), float('inf'))
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

# Interactive game
total = 0
print("\nYou are Player 1 (maximizer), Computer is Player 2 (minimizer)")
player_first = input("Do you want to go first? (y/n): ").lower() == 'y'

if not player_first:
    move = get_best_move(total)
    total += move
    print(f"\nComputer adds {move}. Total: {total}")

while total < 20:
    print(f"\nCurrent total: {total}")
    while True:
        try:
            move = int(input("Your move (1-3): "))
            if 1 <= move <= 3 and total + move <= 20:
                break
            print("Invalid move! Choose 1, 2, or 3 (and don't exceed 20)")
        except ValueError:
            print("Please enter a number!")
    
    total += move
    print(f"→ You added {move}. Total: {total}")
    
    if total == 20:
        print("\n🎉 You win!")
        break
    
    comp_move = get_best_move(total)
    total += comp_move
    print(f"→ Computer adds {comp_move}. Total: {total}")
    
    if total == 20:
        print("\n💻 Computer wins!")
        break
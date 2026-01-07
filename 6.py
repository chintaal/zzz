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
import numpy as np
from queue import PriorityQueue

print("="*50)
print("8-Puzzle Solver using A* Algorithm")
print("="*50)

class State:
    def __init__(self, board, parent, g, h, move=None):
        self.board = board
        self.parent = parent
        self.f = g + h
        self.g = g
        self.move = move

    def __lt__(self, other):
        return self.f < other.f

def display_board(board):
    for row in board:
        print(" ", " ".join(str(x) if x != 0 else ' ' for x in row))

def heuristic(a, b):
    return np.sum(a != b)

def solve(start, goal):
    pq = PriorityQueue()
    pq.put(State(start, None, 0, heuristic(start, goal)))
    visited = set()
    nodes_explored = 0

    print("\n→ Starting A* search...")
    while not pq.empty():
        node = pq.get()
        nodes_explored += 1
        
        if nodes_explored % 100 == 0:
            print(f"  Explored {nodes_explored} nodes...")
        
        if np.array_equal(node.board, goal):
            print(f"✓ Solution found! Explored {nodes_explored} nodes\n")
            return node

        visited.add(str(node.board))
        x, y = np.where(node.board == 0)
        x, y = int(x[0]), int(y[0])
        
        for dx, dy, direction in [(0,1,'right'),(1,0,'down'),(0,-1,'left'),(-1,0,'up')]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = node.board.copy()
                new[x,y], new[nx,ny] = new[nx,ny], new[x,y]
                if str(new) not in visited:
                    pq.put(State(new, node, node.g+1, heuristic(new, goal), direction))
    
    return None

def get_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]

# Get puzzle configuration
print("\nDefault puzzle:")
start = np.array([[2,8,1],[0,4,3],[7,6,5]])
goal = np.array([[1,2,3],[8,0,4],[7,6,5]])

print("\nStart:")
display_board(start)
print("\nGoal:")
display_board(goal)

use_default = input("\nUse default puzzle? (y/n): ").lower() == 'y'

if not use_default:
    print("\nEnter start configuration (use 0 for empty space):")
    start = np.array([[int(x) for x in input(f"Row {i+1} (3 numbers): ").split()] for i in range(3)])

print("\n" + "="*50)
solution = solve(start, goal)

if solution:
    path = get_path(solution)
    print(f"📊 Solution found in {len(path)-1} moves:\n")
    
    for i, state in enumerate(path):
        print(f"Step {i}:" + (f" (Move {state.move})" if state.move else ""))
        display_board(state.board)
        print()
    
    print(f"✓ Puzzle solved!")
else:
    print("✗ No solution found!")

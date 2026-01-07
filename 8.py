import numpy as np
from queue import PriorityQueue

class State:
    def __init__(self, board, parent, g, h):
        self.board = board
        self.parent = parent
        self.f = g + h
        self.g = g

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return np.sum(a != b)

def solve(start, goal):
    pq = PriorityQueue()
    pq.put(State(start, None, 0, heuristic(start, goal)))
    visited = set()

    while not pq.empty():
        node = pq.get()
        if np.array_equal(node.board, goal):
            return node

        visited.add(str(node.board))
        x, y = np.where(node.board == 0)
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = node.board.copy()
                new[x,y], new[nx,ny] = new[nx,ny], new[x,y]
                if str(new) not in visited:
                    pq.put(State(new, node, node.g+1, heuristic(new, goal)))

start = np.array([[2,8,1],[0,4,3],[7,6,5]])
goal = np.array([[1,2,3],[8,0,4],[7,6,5]])

solution = solve(start, goal)

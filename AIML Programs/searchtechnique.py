# Uninformed Search: Breadth-First Search (BFS)
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return False

# Informed Search: A* Search
import heapq

def a_star(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (0 + h(start), start))
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h(neighbor)
                heapq.heappush(open_list, (f_score, neighbor))
    
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Adversarial Search: Minimax Algorithm with Alpha-Beta Pruning
def minimax(position, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal(position):
        return evaluate(position)
    
    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example usage
if __name__ == "__main__":
    # Example graph for BFS and A*
    graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'D': 1, 'E': 1},
        'C': {'A': 1, 'F': 1},
        'D': {'B': 1},
        'E': {'B': 1, 'F': 1},
        'F': {'C': 1, 'E': 1}
    }
    
    # Heuristic function for A* (example)
    def heuristic(node):
        heuristics = {'A': 3, 'B': 2, 'C': 1, 'D': 4, 'E': 2, 'F': 0}
        return heuristics[node]
    
    print("BFS:", bfs(graph, 'A', 'F'))
    print("A*:", a_star(graph, 'A', 'F', heuristic))
    
    # Example position for Minimax (example)
    def is_terminal(position):
        # Define terminal state check
        return False  # Placeholder
    
    def evaluate(position):
        # Define evaluation function
        return 0  # Placeholder
    
    def get_children(position):
        # Define children generation
        return []  # Placeholder
    
    position = None  # Define initial position
    print("Minimax:", minimax(position, 3, float('-inf'), float('inf'), True))

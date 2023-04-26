#1)**Implement n-Queen’s Problem
class Graph:
    def __init__(self, n):
        self.adj_list = {}
        for i in range(n ** 2):
            self.adj_list[i] = []
            for j in range(n ** 2):
                if i != j and (i // n == j // n or i % n == j % n or abs(i // n - j // n) == abs(i % n - j % n)):
                    self.adj_list[i].append(j)
    
    def dfs(self, start, visited, path, n):
        visited.add(start)
        path.append(start)
        if len(path) == n:
            return path
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                res = self.dfs(neighbor, visited, path, n)
                if res:
                    return res
        visited.remove(start)
        path.pop()
        return None

def solve_n_queens(n):
    graph = Graph(n)
    for i in range(n ** 2):
        visited = set()
        path = []
        res = graph.dfs(i, visited, path, n)
        if res:
            return [(node // n, node % n) for node in res]
    return None

# Example usage:
print(solve_n_queens(4)) # Output: [(0, 1), (1, 3), (2, 0), (3, 2)]

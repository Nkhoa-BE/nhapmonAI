from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, u):
        visited = [False] * 9  # Có 9 đỉnh: 0 đến 8

        queue = []
        visited[u] = True
        queue.append(u)

        while queue:
            u = queue.pop(0)
            print(u, end=' ')

            for i in self.graph[u]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph()

    # Tạo các cạnh theo hình
    g.addEdge(0, 1)  # S -> A
    g.addEdge(0, 2)  # S -> B
    g.addEdge(0, 3)  # S -> C
    g.addEdge(1, 4)  # A -> D
    g.addEdge(1, 5)  # A -> E
    g.addEdge(2, 6)  # B -> G
    g.addEdge(3, 7)  # C -> F
    g.addEdge(4, 8)  # D -> H

    print("BFS - duyệt tìm kiếm chiều rộng bắt đầu từ đỉnh 0 (S):")
    g.BFS(0)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Thêm cạnh vào đồ thị
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Hàm đệ quy hỗ trợ DFS
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    # Hàm DFS chính
    def DFS(self, v):
        # Tính tổng số đỉnh lớn nhất từ tất cả các đỉnh xuất hiện
        vertices = set(self.graph.keys())
        for adj in self.graph.values():
            vertices.update(adj)
        n = max(vertices) + 1

        visited = [False] * n
        self.DFSUtil(v, visited)

if __name__ == '__main__':
    g = Graph()

    # Thêm các cạnh vào đồ thị
    g.addEdge(0, 1)  
    g.addEdge(0, 2)  
    g.addEdge(0, 3)  
    g.addEdge(1, 4)  
    g.addEdge(1, 5)  
    g.addEdge(4, 6)  
    g.addEdge(5, 7) 

    print("DFS - Duyệt tìm kiếm từ vertex 0")
    g.DFS(0)

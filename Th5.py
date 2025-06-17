from collections import deque

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # Hàm heuristic có giá trị bằng nhau cho tất cả các nút
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'Z': 1
        }
        return H[n]

    def heuristic_alg(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])

        poo = {}
        poo[start] = 0

        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            for v in open_lst:
                if n is None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None
if __name__ == '__main__':
    adjac_lis = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 10), ('E', 12)],
        'C': [('A', 2), ('E', 7)],
        'D': [('B', 10), ('E', 6), ('Z', 15)],
        'E': [('B', 12), ('C', 7), ('D', 6), ('Z', 9)],
        'Z': [('D', 15), ('E', 9)]
    }

    g = Graph(adjac_lis)
    start_node = str(input("Enter the start node: "))
    stop_node = str(input("Enter the stop node: "))
    g.heuristic_alg(start_node, stop_node)
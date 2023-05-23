class Edge:
    def __init__(self, v, u, w):
        self.v = v
        self.u = u
        self.w = w

    def __to_str(self):
        return f"({self.v} - {self.u}):{self.w}"

    def __str__(self):
        return self.__to_str()

    def __repr__(self):
        return self.__to_str()


class MinHeap:
    def __init__(self, key: callable):
        self.__heap = []
        self.key = key
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self.__heap):
            el = self.__heap[self._current_index]
            self._current_index += 1
            return el


        self._current_index = 0
        raise StopIteration

    def add(self, e: object):
        self.__heap.append(e)
        self.__heap = sorted(self.__heap, key=self.key, reverse=False)

    def get(self):
        return self.__heap.pop()

    def __str__(self):
        return ', '.join(list(map(lambda e: str(e), self.__heap)))


class Sets:
    def __init__(self):
        self.parent = [None] * 10000
        self.rank = [None] * 1000

    def add_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
            if i != self.parent[i]:
                self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def trace(self, i):
        trace = []
        while i != self.parent[i]:

            i = self.parent[i]
            if i != self.parent[i]:
                trace.append(i)
                self.parent[i] = self.find(self.parent[i])
        return trace

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id

        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[i_id] + 1


class Graph:
    def __init__(self):
        self.edges = MinHeap(lambda e: e.w)

    def add_edge(self, edge: Edge):
        self.edges.add(edge)

    def __str__(self):
        return str(self.edges)


class KMST:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.sets = Sets()

    def create_map(self):
        for edge in self.graph.edges:
            self.sets.add_set(edge.v)
            self.sets.add_set(edge.u)

    def find_tree(self):
        for edge in self.graph.edges:
            u_id = self.sets.find(edge.u)
            v_id = self.sets.find(edge.v)
            if u_id != v_id:
                self.sets.union(u_id, v_id)
                print(edge)

g = Graph()

g.add_edge(Edge(1, 4, 1))
g.add_edge(Edge(1, 2, 6))
g.add_edge(Edge(2, 3, 2))
g.add_edge(Edge(4, 3, 0))
g.add_edge(Edge(3, 4, 8))
g.add_edge(Edge(4, 5, 1))
g.add_edge(Edge(5, 3, 10))




kmst = KMST(g)
kmst.create_map()
kmst.find_tree()
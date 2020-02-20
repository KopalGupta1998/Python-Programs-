import random
class KargerMinCutter:
    def __init__(self):
        self._graph={1:[2,3,4],2:[1,4],3:[1,4],4:[1,2,3]}
        self._total_edges=5
    def find_min_cut(self):
        min_cut=0
        while len(self._graph)>2:
            v1,v2=self.pick_random_edge()
            self._total_edges-=len(self._graph[v1])
            self._total_edges-=len(self._graph[v2])
            self._graph[v1].extend(self._graph[v2])
            for vertex in self._graph[v2]:
                self._graph[vertex].remove(v2)
                self._graph[vertex].append(v1)
            self._graph[v1] = list(filter(lambda v: v != v1, self._graph[v1]))
            self._total_edges+=len(self._graph[v1])
            self._graph.pop(v2)
        for edges in self._graph.values():
            min_cut=len(edges)
        return min_cut
            
    def pick_random_edge(self):
        rand_edge=random.randint(0,self._total_edges-1)
        for vertex,vertex_edges in self._graph.items():
            if len(vertex_edges)<=rand_edge:
                rand_edge-=len(vertex_edges)
            else:
                from_vertex=vertex
                to_vertex=vertex_edges[rand_edge]
                return from_vertex,to_vertex

if __name__ == "__main__":
    min_cut = 99999
    for i in range(4):
        min_cutter = KargerMinCutter()
        cut = min_cutter.find_min_cut()
        if cut < min_cut:
            min_cut = cut
        print(min_cut)

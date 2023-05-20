import vertex
class Graph:
    def __init__(self) -> None:
        self._vertexes = []
    
    
    def add_vertex(self, vertex):
        if vertex not in self._vertexes:
            self._vertexes.append(vertex)
    
    def add_edge(vertex_a,vertex_b, bidirectional= False):
        vertex_a.add_neighbor(vertex_b, bidirectional)
        

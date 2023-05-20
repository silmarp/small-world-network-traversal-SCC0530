import vertex
class Graph:
    def __init__(self) -> None:
        self._vertexes = []
    
    
    def add_vertex(self, vertex):
        if vertex not in self._vertexes:
            self._vertexes.append(vertex)
    
    def add_edge(self, vertex_a,vertex_b, bidirectional= False):
        vertex_a.add_neighbor(vertex_b, bidirectional)
    
    def depth_first_search(self, origin, destination):
        visited = set()
        path = self.__recur_depth_first_search(origin, destination, visited)
        if path:
            return path
        else:
            return []


    def __recur_depth_first_search(self, current, destination, visited):
        visited.add(current)

        if destination == current:
            return [destination]

        neighbors = []
        for vertex in self._vertexes:
            if vertex._label == current:
                neighbors = vertex._neighbors
            
        for neighbor in neighbors:
            stack = []
            if neighbor not in visited:
                stack = self.__recur_depth_first_search(neighbor[0]._label, destination, visited)
    
            if stack is not None:
                stack.insert(0, current)
                return stack


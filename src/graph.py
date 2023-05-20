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
        for vertex in self._vertexes:
            if origin == vertex._label:
                origin = vertex
            elif destination == vertex._label:
                destination = vertex
        path = self.__recur_depth_first_search(origin, destination, visited)
        if path:
            return path
        else:
            return []


    def __recur_depth_first_search(self, current, destination, visited):
        visited.add(current)

        if destination == current:
            return [destination._label]

        for neighbor in current._neighbors:
            stack = []
            if neighbor not in visited:
                stack = self.__recur_depth_first_search(neighbor[0], destination, visited)
    
            if stack is not None:
                stack.insert(0, current._label)
                return stack

    def breadth_first_search(self, origin, destination):
        visited = set()
        for vertex in self._vertexes:
            if origin == vertex._label:
                origin = vertex
            elif destination == vertex._label:
                destination = vertex

        path = self.__recur_breadth_first_search(origin, destination, visited, [])
        if path:
            return path
        else:
            return []

    def __recur_breadth_first_search(self, current, destination, visited, queue):
        visited.add(current)

        if current == destination:
            return [current._label]

        for neighbor in current._neighbors:
            if neighbor not in visited:
                queue.append(neighbor[0])

        path = self.__recur_breadth_first_search(queue[0], destination, visited, queue[1::])
        if path is not None:
            path.insert(0, current._label)
            return path


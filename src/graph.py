import sys
import vertex
import math
class Graph:
    def __init__(self) -> None:
        self._vertexes = []
    
    
    def add_vertex(self, vertex):
        if vertex not in self._vertexes:
            self._vertexes.append(vertex)
    
    def add_edge(self, vertex_a,vertex_b, bidirectional= False):
        vertex_a.add_neighbor(vertex_b, bidirectional)
    
    def add_vertices(self, vertices):
        for v in vertices:
            self.add_vertex(v)

    def get_distance(self, path):
        vertexes = []
        for index, p in enumerate(path):
            for vertex in self._vertexes:
                if p == vertex._label:
                    vertexes.append(vertex)

        distance = 0
        for index, vertex in enumerate(vertexes):
            if index < len(path)-1:
                distance += math.dist([vertex._x, vertex._y], [vertexes[index+1]._x, vertexes[index+1]._y])
        return distance

    def depth_first_search(self, origin, destination):
        for vertex in self._vertexes:
            if str(origin) == vertex._label:
                origin = vertex
            elif str(destination) == vertex._label:
                destination = vertex

        visited = []
        stack = []
        path = []

        stack.append(origin)
        while stack:
            vertex = stack.pop()
            path.append(vertex._label)
            if vertex._label not in visited:
                visited.append(vertex._label)
            elif vertex._label in visited:
                continue
            if vertex._label == destination:
                break

            for neighbor in vertex._neighbors:
                stack.append(neighbor[0])

        return path
        
    """
        path = self.__recur_depth_first_search(origin, destination, visited)
        if path:
            return path
        else:
            return []
"""

    def __recur_depth_first_search(self, current, destination, visited):
        #visited.append(current)
        visited.append(current._label)

        if destination == current:
            return visited
            #return [destination._label]

        for neighbor in current._neighbors:
            stack = []
            if neighbor not in visited:
                stack = self.__recur_depth_first_search(neighbor[0], destination, visited)
    
            if stack is not None:
                return stack
                """
                stack.insert(0, current._label)
                return stack
                """

    def breadth_first_search(self, origin, destination):
        visited = []
        for vertex in self._vertexes:
            if str(origin) == vertex._label:
                origin = vertex
            elif str(destination) == vertex._label:
                destination = vertex

        path = self.__recur_breadth_first_search(origin, destination, visited, [])
        if path:
            return path
        else:
            return []

    def __recur_breadth_first_search(self, current, destination, visited, queue):
        visited.append(current._label)
        #visited.append(current)

        if current == destination:
            return visited
            #return [current._label]

        for neighbor in current._neighbors:
            if neighbor not in visited:
                queue.append(neighbor[0])

        path = self.__recur_breadth_first_search(queue[0], destination, visited, queue[1::])
        if path is not None:
            return path
            """
            path.insert(0, current._label)
            return path
            """

    def best_first_search(self, origin, destination):
        from queue import PriorityQueue

        for vertex in self._vertexes:
            if str(origin) == vertex._label:
                origin = vertex
            elif str(destination) == vertex._label:
                destination = vertex

        # Tiebreaker value in case of equal weight
        count = 0
        pq = PriorityQueue()
        pq.put((0, count, origin))

        visited = []
        visited.append(origin._label)
        
        path = []

        while not pq.empty():
            current = pq.get()[2]
            
            path.append(current._label)
            if current is destination:
                break
            for neighbor in current._neighbors:
                count += 1
                if neighbor[0]._label not in visited:
                    visited.append(neighbor[0]._label)
                    pq.put((neighbor[1], count, neighbor[0]))
        #return path
        return visited

    def a_star_search(self, origin, destination):
        from queue import PriorityQueue

        for vertex in self._vertexes:
            if str(origin) == vertex._label:
                origin = vertex
            elif str(destination) == vertex._label:
                destination = vertex

        # Tiebreaker value in case of equal weight
        count = 0
        pq = PriorityQueue()
        pq.put((0, count, origin))

        visited = set()
        visited.add(origin)

        path = []

        while not pq.empty():
            current = pq.get()[2]

            path.append(current._label)
            if current is destination:
                break
            for neighbor in current._neighbors:
                count += 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    pq.put((neighbor[1]+neighbor[0].dist(destination), count, neighbor[0]))
        return path
    
    
    def dijkstra(self, origin):
        for vertex in self._vertexes:
            if str(origin) == vertex._label:
                origin = vertex
        
        unvisited_nodes = list([i for i in self._vertexes])
        
        shortest_path = {}
        previous_node = {}
        max_value = sys.maxsize
        
        
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[origin]
        
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = current_min_node._neighbors
            for neighbor in neighbors:
                new_dist = shortest_path[current_min_node]+ current_min_node[neighbor]
                if new_dist < shortest_path[neighbor]:
                    shortest_path[neighbor] = new_dist
                    previous_node[neighbor] = current_min_node
            
            unvisited_nodes.remove[current_min_node]
        
        return previous_node, shortest_path
	
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
                    
                
            

        

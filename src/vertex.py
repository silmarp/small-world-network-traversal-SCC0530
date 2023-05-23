class Vertex:
    def __init__(self, x, y,  label = '') -> None:
        self._label = label
        self._x = x
        self._y = y
        self._neighbors = []
    
    def add_edge(self, n_vertex, weight = 0, bidirectional = False):
        if n_vertex not in self.get_neighbors_vertices():
            self._neighbors.append((n_vertex, weight))
        if bidirectional:
            n_vertex.add_edge(self,weight)
    
    def remove_edge(self, vertex, bidirectional = False):
        vertex_to_remove = []
        for i in range(len(self.get_neighbors())):
            if self._neighbors[i][0] == vertex:
                self._neighbors.remove(self._neighbors[i])
                if bidirectional:
                    vertex.remove_edge(self)
                break
                    
    
    def get_neighbors(self):
        return self._neighbors

    def get_neighbors_vertices(self):
        vertices = []
        
        for v in self.get_neighbors():
            vertices.append(v[0])
        
        return vertices
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_label(self):
        return self._label
    
    def dist(self, vertex):
        from math import dist
        return dist([self.get_x(), self.get_y()], [vertex.get_x(), vertex.get_y()])
    
    def __str__(self):
        repr_v = ""
        if self.get_label() != '':
            repr_v = self.get_label() + " " +"{:.2f}".format(self.get_x()) + " " + "{:.2f}".format(self.get_y()) + ":"
        else:
            repr_v = str(self.get_x()) + " " + str(self.get_y()) + ": "
        for i in self.get_neighbors(): 
            repr_v = repr_v +" ("+i[0].get_label() + ", " + "{:.2f}".format(i[1]) + ")"
        return repr_v
    
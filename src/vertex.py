class Vertex:
    def __init__(self,x,y, label = '') -> None:
        self._label = label
        self._x = x
        self._y = y
        self._neighbors = []
    
    def add_neighbor(self,n_vertex, weight = 0, bidirectional = False):
        if self not in n_vertex.get_neighbors():
            self._neighbors.append((n_vertex, weight))
        if bidirectional:
            n_vertex.add_neighbor(self)
    
    def get_neighbors(self):
        return self._neighbors
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_label(self):
        return self._label
    
    
    def __str__(self):
        return (self._label)
    
    def __repr__(self):
        return(self._label+": "+str(self._neighbors))
    
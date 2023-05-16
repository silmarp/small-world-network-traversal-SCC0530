class Graph:
    def __init__(self, g_dict = None, is_bidirectional = False):
        """
        graph = {
            vertex1: [edge, edge, ...],
            vertex2: [edge, edge, ...],
            ...,
            vertexN: [edge, edge, ...],
        }
        edge = (connectedVertex, weight)
        """

        if g_dict is None:
            g_dict = {}

        self._g_dict = g_dict

        # True: if A -> B then B -> A
        self._bidirectional = is_bidirectional

    def add_edge(self, origin, destination, weight=1):
        # if first time vertex, add it to graph
        if origin not in self._g_dict.keys():
            self._g_dict[origin] = []
        if destination not in self._g_dict.keys():
            self._g_dict[destination] = []

        # add vertex & weight to edges list
        if self._bidirectional:
            self._g_dict[origin].append((destination, weight))
            self._g_dict[destination].append((origin, weight))
        else:
            self._g_dict[origin].append((destination, weight))



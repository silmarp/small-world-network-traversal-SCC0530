import graphviz  # doctest: +NO_EXE
import graph
import vertex as v
import knn_generator as knn

def visualize_graph(vertices, edges, path=None):
    dot = graphviz.Graph(engine='circo')
    for vertex in vertices:
        print(vertex._label)
        dot.node(vertex._label, vertex._label, pos=f'{vertex._x},{vertex._y}!', color="blue")
    if path != None: 
        path = [vertex + path[index+1] for index, vertex in enumerate(path) if index < len(path)-1]
        print(path)
        pairs = []
        for edge in edges:
            for neighbor, _ in edge._neighbors:
                pair = f"{edge._label}{neighbor._label}"
                if pair not in pairs:
                    if pair in path or pair[::-1] in path:
                        dot.edge(edge._label, neighbor._label, color="red")
                    else:
                        dot.edge(edge._label, neighbor._label)
                    pairs.append(pair)
                    pairs.append(pair[::-1])
    else:
        pairs = []
        for edge in edges:
            for neighbor, _ in edge._neighbors:
                pair = f"{edge._label}{neighbor._label}"
                if pair not in pairs:
                    dot.edge(edge._label, neighbor._label)
                    pairs.append(pair)
                    pairs.append(pair[::-1])
 
    return dot.source

"""
def main():
    gr = graph.Graph()
    vertices = knn.generate_vertices(5)

    edges = knn.generate_edges(vertices,2)
    path = ['1', '2', '3']
    print("oopss")
    print(visualize_graph(vertices, edges, path=path))



if __name__ == "__main__":
    main()
"""

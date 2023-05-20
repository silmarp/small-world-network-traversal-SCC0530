import graph
import vertex as v
import knn_generator as knn

def main():
    gr = graph.Graph()
    vertices = knn.generate_vertices(5)
    for i in vertices:
        print(i)
    
    vertices = knn.generate_edges(vertices,2)
    for i in vertices:
        print(i)
    
 

if __name__ == "__main__":
    main()

import graph
import vertex as v
import knn_generator as knn
import small_world_gen as swg

def main():
    gr = graph.Graph()
    
    vertices = knn.generate_vertices(10)

    vertices = swg.generate_edges(vertices,3,0.5)
    
    for i in vertices:
        print(i)



if __name__ == "__main__":
    main()

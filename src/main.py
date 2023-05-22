import graph
import vertex as v
import knn_generator as knn
import small_world_gen as swg

def main():
    gr = graph.Graph()
    
    vertices = knn.generate_vertices(100)

    vertices = swg.generate_edges(vertices,20,0.5)
    
    for i in vertices:
        print(i)
        print()
        
    for v in vertices:
        gr.add_vertex(v)
    print(gr.a_star_search('1','35'))


if __name__ == "__main__":
    main()

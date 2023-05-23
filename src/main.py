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

def experiment_1():
    # Generate Small world min 100 vertices

    # apply each search alg to graph after selecting 2 random vertices of start and finish

    # generate visualization for Graph

    # generate visualization for each Path

def experiment_2():
    # generate small world graphs for each configuration
    #(n=2000, k=7, p=10%)
    #(n=2000, k=7, p=7%)
    #(n=2000, k=7, p=1%)

    # apply all search algs and report medium distance, and time of each alg

def experiment_3():
    #use experiment 2 networks to compare dijkstra with A* algoritm


    


if __name__ == "__main__":
    main()

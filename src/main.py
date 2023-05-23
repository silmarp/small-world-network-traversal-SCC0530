import graph
import vertex as v
import knn_generator as knn
import small_world_gen as swg
import visualize

def main():
    experiment_1()
    """
    gr = graph.Graph()
    vertices = swg.generate_vertices(500)

    gr._vertexes = vertices
    

    edges = swg.generate_edges(vertices,3,0.5)

    for v in edges:
        gr.add_vertex(v)
    
    path = gr.breadth_first_search(0,9)
    print(f"the path is{path}")
    # graphviz = visualize.visualize_graph(vertices, edges, path = path)

    # print(graphviz)
    """
def experiment_1():
    # Generate Small world min 100 vertices
    gr = graph.Graph()
    vertices = swg.generate_vertices(100)
    gr._vertexes = vertices
    edges = swg.generate_edges(vertices, 5, 0.6)

    for v in edges:
        gr.add_vertex(v)

    dot = visualize.visualize_graph(vertices, edges)
    print(f"Original Graph:\n{dot}")

    # apply each search alg to graph after selecting 2 random vertices of start and finish
    targets = [2, 85]
    print(f"Search from {targets[0]} to destination {targets[1]}")

    bfs_path = gr.breadth_first_search(targets[0], targets[1])
    distance = gr.get_distance(bfs_path)
    print(f"Method: Breadt first\nDistance: {distance}\nPath:{bfs_path}\n")

    
    dfs_path = gr.depth_first_search(targets[0], targets[1])
    distance = gr.get_distance(dfs_path)
    print(f"Method: Depth first\nDistance: {distance}\nPath:{dfs_path}\n")

    bestfs_path = gr.best_first_search(targets[0], targets[1])
    dist = gr.get_distance(bestfs_path)
    print(f"Method: Best first\nDistance:{dist}\nPath:\n{bestfs_path}")

    

    astarfs_path = gr.a_star_search(targets[0], targets[1])
    dist = gr.get_distance(astarfs_path)
    print(f"Method: A Star\nDistance:{dist}\nPath:\n{astarfs_path}")

def experiment_2():
    # generate small world graphs for each configuration
    #(n=2000, k=7, p=10%)
    #(n=2000, k=7, p=7%)
    #(n=2000, k=7, p=1%)

    # apply all search algs and report medium distance, and time of each alg
    return

def experiment_3():
    #use experiment 2 networks to compare dijkstra with A* algoritm
    return
    


if __name__ == "__main__":
    main()

import graph
import vertex as v
import knn_generator as knn
import small_world_gen as swg
import visualize
import random
import signal
import time

def main():
    experiment_2_10()
    print("\n")
    experiment_2_07()
    print("\n")
    experiment_2_01()
    print("\n")
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

def experiment_2_10():
    #(n=2000, k=7, p=10%)
    print(f"Network Parameters: n=2000, k=7, p=10%")
    gr = graph.Graph()
    vertices = swg.generate_vertices(2000)
    gr._vertexes = vertices
    edges = swg.generate_edges(vertices, 7, 0.10)

    for v in edges:
        gr.add_vertex(v)
    
    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.breadth_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Breadt_First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.depth_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Depth_First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.best_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Best First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.a_star_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: A Star\nMedium distance:{distance/10}\nMedium time: {final_time/10}")


def experiment_2_07():
    #(n=2000, k=7, p=7%)
    print(f"Network Parameters: n=2000, k=7, p=7%")
    gr = graph.Graph()
    vertices = swg.generate_vertices(2000)
    gr._vertexes = vertices
    edges = swg.generate_edges(vertices, 7, 0.07)

    for v in edges:
        gr.add_vertex(v)
    
    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.breadth_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Breadt_First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.depth_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Depth_First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.best_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Best First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.a_star_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: A Star\nMedium distance:{distance/10}\nMedium time: {final_time/10}")





def experiment_2_01():
    #(n=2000, k=7, p=1%)
    print(f"Network Parameters: n=2000, k=7, p=1%")
    gr = graph.Graph()
    vertices = swg.generate_vertices(2000)
    gr._vertexes = vertices
    edges = swg.generate_edges(vertices, 7, 0.01)

    for v in edges:
        gr.add_vertex(v)
    
    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.breadth_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Breadt_First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.depth_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Depth_First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.best_first_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: Best First\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

    distance = 0
    final_time = 0
    for i in range(9):
        origin = random.randint(0, 1999)
        destination = random.randint(0, 1999)
        
        start_time = time.time()
        path = gr.a_star_search(origin, destination)
        distance += gr.get_distance(path)
        final_time += time.time() - start_time

    print(f" Method: A Star\nMedium distance:{distance/10}\nMedium time: {final_time/10}")

def experiment_3():
    #use experiment 2 networks to compare dijkstra with A* algoritm
    return
    


if __name__ == "__main__":
    main()

import knn_generator as knn

def generate_vertices(n, seed = None):
    return knn.generate_vertices(n, seed)

def generate_edges(vertices, k, p, seed = None):
    import random
    vertices = knn.generate_edges(vertices,k)
    if seed is not None:
       random.seed(seed)
    
    vtr = []
    vta = []
    
    for v in vertices:
        for n in v.get_neighbors():
            pp = random.random()
            if p>pp:
                vtr.append(n)
                new_n = vertices[random.randint(0,len(vertices)-1)]
                while new_n == v:
                    new_n = vertices[random.randint(0,len(vertices)-1)]
                vta.append(new_n)
        for i in range(len(vtr)):
            v.remove_edge(vtr[i][0], bidirectional = True)
            v.add_edge(vta[i],v.dist(vta[i]), bidirectional = True)

    return vertices
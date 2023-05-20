import graph as g
import vertex as v
import random

def generate_vertices(n):
        vertices = []
        for i in range(n):
            x = random.random()*n
            y = random.random()*n
            vertices.append(v.Vertex(x,y,str(i)),)
        return vertices
    
def generate_edges(vertices, k):
    for v in vertices:
        dist = []
        max_d = 0
        for u in vertices:
            if u!=v:
                d_u = v.dist(u)
                #less than k neighbors, just append and update max dist
                if len(dist)<k:
                    dist.append((u,d_u))
                    if d_u > max_d:
                        max_d = d_u
                else:
                    #more than k neighbors
                    if d_u < max_d:
                        d = 0
                        for i in range(len(dist)):
                            if dist[i][1] == max_d:
                                dist[i]=(u,d_u)
                            else:
                                d = max(d,dist[i][1])
                        max_d = max(d,d_u)
        for u in dist:
            v.add_edge(u[0],u[1],True)
    return vertices      
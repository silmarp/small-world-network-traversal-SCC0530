import graph
import vertex

def main():
    gr = graph.Graph()
    a = vertex.Vertex(1,1,'a')
    b = vertex.Vertex(2,2,'b')
    a.add_neighbor(b)
    gr.add_vertex(a)
    gr.add_vertex(b)
 

if __name__ == "__main__":
    main()

import graphs

def main():
    g = graphs.Graph(g_dict = {
        "a": [("b",1)],
        "b": [("a",1)]
    }, is_bidirectional=True)

    g.add_edge("c", "a")
    print(g._g_dict)

if __name__ == "__main__":
    main()

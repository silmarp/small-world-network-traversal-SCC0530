import graphs

def main():
    g = graphs.Graph(g_dict = {
        "a": [("b",1), ("c", 1)],
        "b": [("d",1), ("e",1)],
        "c": [("f",1),("g",1),],
        "d": [("h",1), ("i", 1), ("j",1),],
        "e": [("j",5), ("k", 1)],
        "f": [("l",1), ("m", 1)],
        "g": [("n",1), ("o", 1)],
        "h": [],
        "i": [],
        "j": [],
        "k": [],
        "l": [],
        "m": [],
        "n": [],
        "o": [],
    }, is_bidirectional=False)

    """
    res = g.depth_first_search("a", "l")
    print(res)
    """

    """
    res = g.breadth_first_search("a", "c")
    print(res)
    """
    res = g.best_first_search("a", "j")
    print(res)
 
 

if __name__ == "__main__":
    main()

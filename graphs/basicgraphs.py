basic_graph = {
    "a":["b","c"],
    "b":["e"],
    "e":["f"],
    "d":["q"],
    "q":[],
    "f":[],
    "c":["d"]
}

def depth_first_traversal(graph:dict,source:str) -> None:
    """ depth first algo by iterative way of solving"""
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)
        for neighbour in basic_graph[current]:
            stack.append(neighbour)

def depth_first_traversal_recursive(graph:dict,source:str) -> None:
    print(source)
    for neighbour in graph[source]:
        depth_first_traversal(graph,neighbour)

def breadth_first_iterative(graph:dict,source:str) -> None:
    queue = [source]
    while queue:
        current = queue.pop(0)
        print(current) 
        for neighbour in basic_graph[current]:
            queue.append(neighbour)
        


depth_first_traversal(basic_graph,"a")
breadth_first_iterative(basic_graph,"a")
depth_first_traversal_recursive(basic_graph,"a")
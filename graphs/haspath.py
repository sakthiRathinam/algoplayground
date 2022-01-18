basic_graph = {
    "a":["b","c"],
    "b":["e"],
    "e":["f"],
    "d":["q"],
    "q":["b"],
    "f":[],
    "c":["d"]
}


def depth_first_path(graph:dict,start:str,dest:str) -> bool:
    if start == dest:
        return True
    for neighbour in graph[start]:
        if depth_first_path(graph,neighbour,dest):
            return True
    return False

def breadth_first_path(graph:dict,start:str,dest:str) -> None:
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False


print(depth_first_path(basic_graph,"b","f"))
print(breadth_first_path(basic_graph,"b","f"))
print(breadth_first_path(basic_graph,"d","a"))
print(depth_first_path(basic_graph,"d","a"))




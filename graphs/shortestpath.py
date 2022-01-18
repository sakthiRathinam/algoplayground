edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]


def breadth_first_short(graph:dict,source:str,dest:str):
    visited = set()
    queue = [(source,0)]
    while queue:
        current,distance = queue.pop(0)
        if current == dest:
            return distance
        visited.add(current)
        print(graph[current])
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append((neighbour,distance+1))
    return -1

def build_graph(array:list):
    graph = dict()
    for edge in array:
        edge1,edge2 = edge
        if edge1 not in graph:
            graph[edge1] = []
        if edge2 not in graph:
            graph[edge2] = []
        graph[edge1].append(edge2)
        graph[edge2].append(edge1)
    return graph


def shortest_path():
    graph = build_graph(edges)
    print(breadth_first_short(graph,'w','z'))


shortest_path()
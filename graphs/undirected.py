array_of_bidirected = [['a','b'],['l','i'],['l','b'],['l','j'],['c','q']]
from typing import List,Optional
def build_adjacency_graph(array:list) -> dict:
    basic_graph = dict()
    for edge in array:
        if edge[0] not in basic_graph:
            basic_graph[edge[0]] = []
        if edge[1] not in basic_graph:
            basic_graph[edge[1]] = []
        basic_graph[edge[0]].append(edge[1]) 
        basic_graph[edge[1]].append(edge[0])
    return basic_graph

def depth_first_unidirectional(graph:dict,source:str,dest:str,visited:set) -> bool:
    if source in visited:
        return False
    if source == dest:
        return True
    visited.add(source)
    for neighbour in graph[source]:
        if depth_first_unidirectional(graph,neighbour,dest,visited):
            return True
    return False

def breadth_first_unidirectional(graph:dict,source:str,dest:str,visited:set) -> bool:
    queue = [source]
    while queue:
        current = queue.pop(0)
        if current == dest:
            return True
        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
    return False
        
def bidirected_graph():
    graph = build_adjacency_graph(array_of_bidirected)
    print(depth_first_unidirectional(graph,'b','j',set()))
    print(breadth_first_unidirectional(graph,'a','q',set()))

bidirected_graph() 
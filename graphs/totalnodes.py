
basic_graph = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}


def depth_first_explore(graph:dict,source:str,visited:set):
    if source in visited:
        return False
    visited.add(source)
    for neighbour in graph[source]:
        depth_first_explore(graph,neighbour,visited)
    return True
def total_nodes():
    total_nodes = 0
    visited = set()
    for node in basic_graph:
        if depth_first_explore(basic_graph,node,visited):
            total_nodes += 1
    return total_nodes

print(total_nodes()) 

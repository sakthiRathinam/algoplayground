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
        return 0
    visited.add(source)
    size = 1
    for neighbour in graph[source]:
        size += depth_first_explore(graph,neighbour,visited)
    return size

def breadth_first_explore(graph:dict,source:str,visited:set):
    if source in visited:
        return 0
    queue = [source]
    size = 0
    while queue:
        current = queue.pop(0)
        size += 1
        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
    return size
def largest_node():
    largest_node = 0
    visited = set()
    for node in basic_graph:
        largest_node = max(depth_first_explore(basic_graph,node,visited),largest_node)
    return largest_node
def breadth_node():
    largest_node = 0
    visited = set()
    for node in basic_graph:
        largest_node = max(breadth_first_explore(basic_graph,node,visited),largest_node)
    return largest_node
print(largest_node()) 
print(breadth_node()) 
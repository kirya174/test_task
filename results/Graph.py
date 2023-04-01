# Реализовать функцию my_code, которая, используя информацию о смежности узлов графа,
# распечатывает достижимые вершины, начиная с переданной

def my_code(graph: dict, node: int, visited_nodes=None):
    print(node)
    if visited_nodes is None:
        visited_nodes = [node]
    for elem in graph[node]:
        if elem not in visited_nodes:
            visited_nodes.append(elem)
            if elem in graph.keys():
                my_code(graph, elem, visited_nodes)
            else:
                print(elem)


def DFS(graph: dict,
        start: int,
        ) -> None:
    visited_nodes = list()
    _stack = list()
    _stack.append(start)
    while _stack:
        v = _stack.pop(0)

        if v in visited_nodes:
            continue
        visited_nodes.append(v)
        print(v)

        if v in graph.keys():
            for node in graph[v]:
                _stack.append(node)

#
data = {
    1: [2, 3],
    2: [4]
}
# my_code(data, 1)
DFS(data, 1)
'''
1
2
4
3
'''

data = {
    1: [2, 3],
    2: [3, 4],
    4: [1]
}
DFS(data, 1)

'''
1
2
3
4
'''

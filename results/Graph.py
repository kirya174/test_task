# Реализовать функцию my_code, которая, используя информацию о смежности узлов графа,
# распечатывает достижимые вершины, начиная с переданной

def dfs(graph: dict,
        start: int,
        ) -> None:

    visited_nodes = set()
    stack = [start]

    while stack:
        v = stack.pop()

        if v in visited_nodes:
            continue
        visited_nodes.add(v)
        print(v)

        if v in graph:
            for node in reversed(graph[v]):
                stack.append(node)

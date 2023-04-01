# Реализовать функцию my_code, которая, используя информацию о смежности узлов графа,
# распечатывает достижимые вершины, начиная с переданной

def dfs(
        graph: dict,
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

        # using graph.get() in case node is not mentioned in graph keys
        stack.extend(reversed(graph.get(v, [])))


def bfs(
        graph: dict,
        start: int
        ) -> None:
    visited_nodes = set()
    queue = [start]

    while queue:
        v = queue.pop(0)

        if v in visited_nodes:
            continue
        visited_nodes.add(v)
        print(v)

        queue.extend(graph.get(v, []))

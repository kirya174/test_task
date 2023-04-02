# Задание 2.
# Реализовать функцию, которая, используя информацию о смежности узлов графа,
# распечатывает достижимые вершины, начиная с переданной

def dfs(
        graph: dict,
        start: int,
        ) -> None:
    """
    Обход графа в глубину, начиная с узла start
    :param graph: Словарь, содержащий граф
    :param start: Начальный узел
    """
    # Заменил список visited_nodes на множество, т.к. необходимо хранить только уникальные значения
    visited_nodes = set()
    # Заменил рекурсивный обход на стэк
    stack = [start]

    while stack:
        v = stack.pop()

        if v in visited_nodes:
            continue
        visited_nodes.add(v)
        print(v)

        # graph.get() используется на случай, если в graph.keys() отсутствует указанный узел
        stack.extend(reversed(graph.get(v, [])))


def bfs(
        graph: dict,
        start: int
        ) -> None:
    """
    Обход графа в ширину, начиная с узла start
    :param graph: Словарь, содержащий граф
    :param start: Начальный узел
    """
    visited_nodes = set()
    queue = [start]

    while queue:
        v = queue.pop(0)

        if v in visited_nodes:
            continue
        visited_nodes.add(v)
        print(v)

        queue.extend(graph.get(v, []))

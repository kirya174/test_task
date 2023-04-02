from itertools import chain

import json


class Component:

    def __init__(self, *algorithm_list):
        self.algorithm_list = algorithm_list

    def __call__(self, source_object):
        result = []
        queue = [source_object]
        while queue:
            result.extend(queue)
            queue = list(chain.from_iterable(
                algorithm(item)
                for item in queue
                for algorithm in self.algorithm_list
            ))
        return result

    def class_capacities(self, object_class) -> dict[str: list]:
        """
        Function returns list of potential paths and list of algorithms
        """
        potential_paths = set()
        algorithms = {}

        for algorithm in self.algorithm_list:
            paths = self.get_paths(algorithm.SPECIFICATION, object_class)
            str_paths = ['/' + '/'.join([elem.__name__ for elem in path]) for path in paths]
            potential_paths.update(str_paths)

        return {"Potential": list(potential_paths),
                "Algorithm": algorithms}

    def get_paths(self, graph: dict, start, path=None) -> list[list]:
        # full path to current node
        path = [start] if path is None else path + [start]
        # adding current node path and it's children (if they exist) to the list of potential paths
        paths = [path] + [path + [node] for node in graph.get(start, [])]
        # iterate over children nodes
        for node in graph.get(start, []):
            # check if child not is already mentioned in path
            if node not in path:
                new_paths = self.get_paths(graph, node, path)
                # adding paths got from children to potential paths list
                for new_path in new_paths:
                    if new_path not in paths:
                        paths.append(new_path)
        return paths


class Apple:
    pass


class Orange:
    def __init__(self, number):
        self.number = number


class Lemon:
    pass


class FirstAlgorithm:
    SPECIFICATION = {
        Orange: [Apple],
        Lemon: [Orange, Apple]
    }

    def __call__(self, source_object):
        if isinstance(source_object, Orange):
            return [
                Apple()
                for _ in range(source_object.number)
            ]
        if isinstance(source_object, Lemon):
            return [Orange(3), Apple()]
        return []


class EmptyAlgorithm:
    SPECIFICATION = {}

    def __call__(self, source_object):
        return []


component = Component(FirstAlgorithm(), EmptyAlgorithm())
print(json.dumps(
    component.class_capacities(Lemon),
    indent=4
))

output = {
    'Potential': [
        '/Lemon',
        '/Lemon/Orange',
        '/Lemon/Apple'
        '/Lemon/Orange/Apple'
    ],
    'Algorithm': {
        'FirstAlgorithm': {
            '/Lemon': [
                '/Lemon/Orange',
                '/Lemon/Apple'
            ],
            '/Lemon/Orange': [
                '/Lemon/Orange/Apple'
            ]
        },
        'EmptyAlgorithm': {}
    }
}

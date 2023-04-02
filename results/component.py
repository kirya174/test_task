from itertools import chain


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

    def class_capacities(self, object_class):
        potential_paths = set()
        algorithm_dict = {}

        for algorithm in self.algorithm_list:
            paths = self.get_paths(algorithm.SPECIFICATION, object_class)
            str_paths = ['/' + '/'.join([elem.__name__ for elem in path]) for path in paths]
            potential_paths.update(str_paths)

        return {"Potential": potential_paths, "Algorithm": algorithm_dict}

    def get_paths(self, graph, start, path=None):
        path = [start] if path is None else path + [start]
        paths = [path] + [path + [node] for node in graph.get(start, [])]
        for node in graph.get(start, []):
            if node not in path:
                new_paths = self.get_paths(graph, node, path)
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

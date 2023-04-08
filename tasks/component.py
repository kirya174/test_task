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
        potential_paths = self._parse_specification(object_class)

        algorithms = dict()
        for algorithm in self.algorithm_list:
            paths = self._get_paths(algorithm.SPECIFICATION, object_class)
            algorithms[self._get_name(algorithm.__class__)] = self._parse_algorithm(paths)

        return {"Potential": list(potential_paths),
                "Algorithm": algorithms}

    def _get_paths(self, graph: dict, start, path=None) -> list[list]:
        # full path to current node
        path = [start] if path is None else path + [start]
        # adding current node path and it's children (if they exist) to the list of potential paths
        paths = [path] + [path + [node] for node in graph.get(start, [])]
        # iterate over children nodes
        for node in graph.get(start, []):
            # check if child not is already mentioned in path
            if node not in path:
                new_paths = self._get_paths(graph, node, path)
                # adding paths got from children to potential paths list
                for new_path in new_paths:
                    if new_path not in paths:
                        paths.append(new_path)
        return paths

    def _parse_specification(self, object_class) -> [set, dict]:
        """
        returns list of potential paths for provided class according to algorithms specifications
        :return: list of unique potential paths
        """
        component_specification = dict()
        # combine specifications of all algorithms to one dictionary
        for algorithm in self.algorithm_list:
            for key, value in algorithm.SPECIFICATION.items():
                component_specification.setdefault(key, []).extend(value)

        # find paths for combined specification
        paths = self._get_paths(component_specification, object_class)

        potential_paths = set()
        # converting them to string representation
        str_paths = ['/' + '/'.join([self._get_name(elem) for elem in path]) for path in paths]
        for path in str_paths:
            potential_paths.add(path)

        return potential_paths

    def _parse_algorithm(self, paths: list[list]) -> dict[dict[list]]:
        """
        returns list of actual paths for provided class according to algorithm's implementation
        :return: dictionary with occurring paths for this algorithm
        """

        result_dict = {}
        # converting list of paths to dictionary
        for elem in [tuple([self._get_name(elem) for elem in path]) for path in paths]:
            # excluding path consisting of 1 element
            if len(elem) > 1:
                key = '/' + '/'.join(elem[:-1])
                value = f'{key}/{elem[-1]}'
                if value not in result_dict.get(key, []):
                    # add key to dict if it doesn't exist, otherwise append value to dict[key]
                    result_dict.setdefault(key, []).append(value)

        return result_dict

    @staticmethod
    def _get_name(obj) -> str:
        return obj.__name__


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


if __name__ == '__main__':
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

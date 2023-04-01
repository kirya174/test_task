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
        potential_paths = [f"/{object_class.__name__}"]
        algorithm_dict = {}

        for algorithm in self.algorithm_list:
            queue = [*algorithm.SPECIFICATION.get(object_class, [])]
            while queue:
                v = queue.pop(0)
                potential_paths.append(f"{potential_paths[0]}/{v.__name__}")
                queue.extend(algorithm.SPECIFICATION.get(v, []))
                # todo only 1st level checked. Need to add check in depth
                # if algorithm.SPECIFICATION.get(v) is not None:
                #     path_n = len(potential_paths) - 1

        return {"Potential": potential_paths, "Algorithm": algorithm_dict}


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

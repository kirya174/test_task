import pytest
from tasks.graph import dfs, bfs

input_data: list[(dict, int)] = [
    ({
         1: [2, 3],
         2: [4]
     },
     1),
    ({
         1: [2, 3],
         2: [3, 4],
         4: [1]
     },
     1),
    ({
         1: []
     },
     1),
    ({
         1: [2],
         2: [3],
         3: [1]
     },
     1),
    ({
         1: [2],
         2: [1],
         3: []
     },
     1),
    ({
         1: [2],
         2: [1],
         4: []
     },
     4),
    ({
         1: [2, 3],
         2: [4],
         3: [4, 5],
         4: [1],
         5: []
     },
     1),
]

expected_result_dfs: list[str] = [
    "1\n2\n4\n3\n",
    "1\n2\n3\n4\n",
    "1\n",
    "1\n2\n3\n",
    "1\n2\n",
    "4\n",
    "1\n2\n4\n3\n5\n"]

dfs_test_data = [(data, start, result) for (data, start), result in zip(input_data, expected_result_dfs)]

expected_result_bfs: list[str] = [
    "1\n2\n3\n4\n",
    "1\n2\n3\n4\n",
    "1\n",
    "1\n2\n3\n",
    "1\n2\n",
    "4\n",
    "1\n2\n3\n4\n5\n"
]

bfs_test_data = [(data, start, result) for (data, start), result in zip(input_data, expected_result_bfs)]


@pytest.mark.parametrize("data, start, expected", dfs_test_data)
def test_graph_dfs(data: dict, start: int, expected: str, capfd):
    dfs(data, start)
    std_out = capfd.readouterr()

    assert std_out.out == expected


@pytest.mark.parametrize("data, start, expected", bfs_test_data)
def test_graph_bfs(data: dict, start: int, expected: str, capfd):
    bfs(data, start)
    std_out = capfd.readouterr()

    assert std_out.out == expected

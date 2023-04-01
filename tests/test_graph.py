import pytest
from Graph import dfs

def test_simple_graph_dfs(capfd):
    data = {
        1: [2, 3],
        2: [4]
    }
    expected = "1\n2\n4\n3\n"

    dfs(data, 1)
    std_out = capfd.readouterr()

    assert std_out.out == expected

def test_recursive_graph_dfs(capfd):
    data = {
        1: [2, 3],
        2: [3, 4],
        4: [1]
    }
    expected = "1\n2\n3\n4\n"

    dfs(data, 1)
    std_out = capfd.readouterr()

    assert std_out.out == expected
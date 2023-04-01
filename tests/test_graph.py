import pytest
from results.Graph import dfs


@pytest.mark.parametrize("data, start, expected",
                         [
                             ({
                                  1: [2, 3],
                                  2: [4]
                              },
                              1,
                              "1\n2\n4\n3\n"),

                             ({
                                  1: [2, 3],
                                  2: [3, 4],
                                  4: [1]
                              },
                              1,
                              "1\n2\n3\n4\n"),

                             ({
                                  1: []
                              },
                              1,
                              "1\n"),

                             ({
                                  1: [2],
                                  2: [3],
                                  3: [1]
                              },
                              1,
                              "1\n2\n3\n"),

                             ({
                                  1: [2],
                                  2: [1],
                                  3: [],
                                  4: []
                              },
                              1,
                              "1\n2\n"),
                             ({
                                  1: [2],
                                  2: [1],
                                  3: [],
                                  4: []
                              },
                              4,
                              "4\n"),
                             ({
                                  1: [2, 3],
                                  2: [4],
                                  3: [4, 5],
                                  4: [1],
                                  5: []
                              },
                              1,
                              "1\n2\n4\n3\n5\n"),
                         ])
def test_simple_graph_dfs(data, start, expected, capfd):
    dfs(data, start)
    std_out = capfd.readouterr()

    assert std_out.out == expected

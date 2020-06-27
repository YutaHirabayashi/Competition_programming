import pytest
from algorhms import bfs

@pytest.mark.parametrize("start_node, node_number, edge_tuple_list, expected", [
    (0, 6, 
    [(1, 2), (0, 3), (0, 5), (1, 4), (3, 5), (2, 4)],
    [0, 1, 1, 2, 3, 2])
])
def test_bfs(start_node, node_number, edge_tuple_list, expected):
    assert bfs(start_node, node_number, edge_tuple_list) == expected
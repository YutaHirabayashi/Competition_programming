import pytest
from algorhms import dfs_partial_sum

@pytest.mark.parametrize("array,sum,expected",[
    ([1,4,5,6,8], 9, True),
    ([1,10,10,30,2],44,False)
])
def test_dfs_partial_sum(array, sum, expected):
    assert dfs_partial_sum(array, sum) == expected
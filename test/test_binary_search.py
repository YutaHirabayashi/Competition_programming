import pytest
from algorhms import binary_search

@pytest.mark.parametrize("array,target,expected",[
    ([1,4,5,6],5,True),
    ([1],2,False),
    ([1,3,4],4,True),
    ([1,2],3,False)
])
def test_binary_search(array, target, expected):
    assert binary_search(array, target) == expected
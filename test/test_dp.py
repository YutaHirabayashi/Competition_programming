from algorhms import dp_knapsack
import pytest

@pytest.mark.parametrize("weight_list, value_list, limited_weight, expected",[
    ([2,1,3,2],[3,2,4,2], 5, 7)
])
def test_dp_knapsack(weight_list, value_list, limited_weight, expected):
    assert dp_knapsack(weight_list, value_list,limited_weight) == expected

from algorhms import dp_knapsack, dp_partial_sum, dp_numbering_partial_sum, dp_minimum_number_partial_sum
import pytest
import numpy as np

@pytest.mark.parametrize("weight_list, value_list, limited_weight, expected",[
    ([2,1,3,2],[3,2,4,2], 5, 7)
])
def test_dp_knapsack(weight_list, value_list, limited_weight, expected):
    assert dp_knapsack(weight_list, value_list,limited_weight) == expected

@pytest.mark.parametrize("array,sum,expected",[
    ([1,4,5,6,8], 9, True),
    ([1,10,10,30,2],44,False)
])
def test_dp_partial_sum(array, sum, expected):
    assert dp_partial_sum(array, sum) == expected

@pytest.mark.parametrize("array, sum, number_divide, expected",[
    ([7, 5, 3, 1, 8], 12, 1000000009, 2),
    ([4, 1, 1, 1], 5, 1000000009, 3)
])
def test_dp_numbering_partial_sum(array, sum, number_divide, expected):
    assert dp_numbering_partial_sum(array, sum, number_divide) == expected

@pytest.mark.parametrize("array, sum, expected",[
    ([7, 5, 3, 1, 8], 12, 2),
    ([7, 5], 6, -1)
])
def test_dp_minimum_number_partial_sum(array, sum, expected):
    assert dp_minimum_number_partial_sum(array, sum) == expected
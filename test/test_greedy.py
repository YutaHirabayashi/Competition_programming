from algorhms import greedy_coin, greedy_dictionary
import pytest

@pytest.mark.parametrize("own_coin_number_dict, price, expected", [
    ({1:3, 5:2, 10:1, 50:3, 100:0, 500:2}, 620, {1:0, 5:2, 10:1, 50:2, 100:0, 500:1})
])

def test_greedy_coin(own_coin_number_dict, price, expected):
    assert greedy_coin(own_coin_number_dict, price) == expected

@pytest.mark.parametrize("from_str_list, expected", [
    (["C", "D", "B", "A", "C"],
    ["C", "A", "B", "C", "D"])
])

def test_greedy_dictionary(from_str_list, expected):
    assert greedy_dictionary(from_str_list) == expected
from algorhms import greedy_coin
import pytest

@pytest.mark.parametrize("own_coin_number_dict, price, expected", [
    ({1:3, 5:2, 10:1, 50:3, 100:0, 500:2}, 620, {1:0, 5:2, 10:1, 50:2, 100:0, 500:1})
])

def test_greedy_coin(own_coin_number_dict, price, expected):
    assert greedy_coin(own_coin_number_dict, price) == expected

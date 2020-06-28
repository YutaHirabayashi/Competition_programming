import numpy as np

def dp_knapsack(weight_list:list, value_list:list, limited_weight:int) -> int:
    """ナップサック問題（DP）

    Args:
        weight_list (list): 重さのリスト
        value_list : 価値のリスト
        limited_weight (int) : 許容される重さ（制約条件）

    Returns:
        int: 積み込める最大の価値

    
    """    
    number_of_baggage = len(weight_list)

    # DPのメモ化用配列
    # dp_value[i][j]:i番目以降の荷物で重さj以下になるように荷物を詰め込んだ際に詰め込める最大の価値
    dp_value = np.zeros((number_of_baggage + 1, limited_weight + 1))

    for i_baggage in reversed(range(number_of_baggage)):
        for j_weight in range(limited_weight + 1):
            if j_weight < weight_list[i_baggage]:
                dp_value[i_baggage, j_weight] = dp_value[i_baggage + 1, j_weight]
            else:
                dp_value[i_baggage, j_weight] = max(
                    dp_value[i_baggage + 1, j_weight], #入れ換えない場合 
                    dp_value[i_baggage + 1, j_weight - weight_list[i_baggage]] + value_list[i_baggage] #入れ換えた場合
                )
    return dp_value[0, limited_weight]
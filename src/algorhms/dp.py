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

def dp_partial_sum(array:list, sum_judge:int)->bool:
    """部分和問題をDPで解く

    Args:
        array (list): 入力の配列
        sum_judge (int): 判定したい部分和

    Returns:
        bool: 部分和問題成立（True）/不成立（False)
    """    

    N = len(array)
    # array[0] ~ array[N-1]
    # dp[SUM][N]
    # dp[j][i]:i番目以降の数字で総和jにできるか？
    #　知りたいもの：dp[SUM][0]

    dp = [[False for i in range(N+1)] for j in range(sum_judge + 1)]

    dp[0][N] = True

    for i in reversed(range(N)):
        for j in range(sum_judge + 1):
            
            if array[i] > sum_judge: #足す余地なし
                dp[j][i] = dp[j][i + 1]
            else:
                dp[j][i] = dp[j][i+1] or dp[j - array[i]][i+1]

    return dp[sum_judge][0]

if __name__ == "__main__":
    dp_partial_sum(
        [1,4,5,6,8], 9
    )
    pass
def dfs_partial_sum(array:list, sum_judge:int, position:int = 0, sum_search:int = 0) -> bool:
    """部分和問題をDFSで解く（再帰関数）

    Args:
        array (list): 入力の配列
        sum_judge (int): 判定したい部分和
        position (int): 現在調査してるindex（外部から最初に関数を使う場合は０）
        sum_search (int): 現在の部分和（外部から最初に関数を使う場合は０）

    Returns:
        bool: True(部分和問題成立)/False(不成立)
    """    
    #全ての配列のTrue／Falseを決定した場合、部分和が成立しているかチェックする（次の値へは進まない）
    if position == len(array) - 1:
        return sum_judge == sum_search

    #枝刈り（現時点で判定したい部分和を超えてる場合、この枝の先に解はないので戻る）
    if sum_search > sum_judge:
        return False
    
    #position番目をTrueとする場合->部分和に追加してposition+1番目の配列に進む
    if dfs_partial_sum(array, sum_judge, position + 1, sum_search + array[position]):
        return True #最下層でTrueが出たら調査終了（position番目をFalseとする場合の調査は行わない）

    #position番目をFalseとする場合->部分和に追加せずposition+1番目の配列に進む
    if dfs_partial_sum(array, sum_judge, position + 1, sum_search):
        return True

    #どこからもTrueが帰らなかった場合、Falseを返す
    return False
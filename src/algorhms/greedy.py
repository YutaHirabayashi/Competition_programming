from collections import deque

def greedy_coin(own_coin_number_dict:dict, price:int) -> dict:
    """硬貨問題を貪欲法で解く

    Args:
        own_coin_number_dict (dict): 所持してるコインの枚数
        price (int): 支払い価格

    Returns:
        dict: 支払うべきコインの枚数

    Example:
        own_coin_number_dict = {1:30, 10:2, 50:1, 100:4}
            -> 1円玉を30枚、10円玉を2枚、50円玉を1枚、100円玉を4枚所持している
    """    
    payment_coin_number_dict = {}
    remaining_price = price

    for coin in sorted(own_coin_number_dict, reverse=True):
        #所持している当該コインの枚数と、残価格を当該コインの価格で割ったもののうち小さい方が支払う枚数
        payment_coin_number = min(int(remaining_price/coin), own_coin_number_dict[coin])
        remaining_price = remaining_price - coin * payment_coin_number
        payment_coin_number_dict[coin] = payment_coin_number
    return payment_coin_number_dict

def greedy_dictionary(from_str_list:list) -> list:
    """辞書順問題を貪欲法で解く
        「入力文字列の先頭もしくは末尾から１文字抜き出して出力文字列に追加」を繰り返した際に辞書順で最小になる出力文字列を求める
    Args:
        from_str_list (list): 入力文字列

    Returns:
        list: 出力文字列
    """    

    to_str_list = []
    queue = deque(from_str_list)
    while queue:
        if list(queue) < list(deque(reversed(queue))):
            s = queue.popleft()
            to_str_list.append(s)
        else:
            s = queue.pop()
            to_str_list.append(s)
    return to_str_list


if __name__ == "__main__":
    greedy_dictionary(
        ["C", "B", "A", "C"]
    )

    greedy_coin(
        {1:3, 5:2, 10:1, 50:3, 100:0, 500:2}, 620
    )
    pass
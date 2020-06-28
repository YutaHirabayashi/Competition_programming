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


if __name__ == "__main__":
    greedy_coin(
        {1:3, 5:2, 10:1, 50:3, 100:0, 500:2}, 620
    )
    pass
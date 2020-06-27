def binary_search(array:list, target:float) -> bool:
    """二分探索

    Args:
        array (list):　検索対象の配列
        target (float): 探したい値

    Returns:
        bool: True（探したい値が含まれている）、False（含まれていない）
    """    
    low = array[0]
    high = array[-1]
    while low <= high:
        mid = (low + high) // 2
        if target >= low and target < mid:
            high = mid
        elif target >= mid and target <= high:
            low = mid
        else:
            return False
        
        if target == high or target == low:
            return True

    return False

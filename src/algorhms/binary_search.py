def binary_search(array:list, target:int) -> bool:
    """二分探索

    Args:
        array (list):　検索対象の配列
        target (int): 探したい値

    Returns:
        bool: True（探したい値が含まれている）、False（含まれていない）
    """    
    low = 0
    high = len(array)-1
    
    if target == array[low] or target == array[high]:
        return True

    while low <= high:
        mid = (low + high) // 2
        if target == array[mid]:
            return True
        
        if target > array[low] and target < array[mid]:
            high = mid
        elif target > array[mid] and target < array[high]:
            low = mid
        else:
            return False
        
        if target == high or target == low:
            return True

    return False

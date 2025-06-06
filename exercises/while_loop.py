def find_first_even(numbers):
    """
    在数字列表中查找第一个偶数
    
    参数:
    - numbers: 整数列表
    
    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            return numbers[index]
        index += 1
    return None


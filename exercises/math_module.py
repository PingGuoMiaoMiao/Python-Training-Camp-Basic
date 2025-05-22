import math

def calculate_square_root(number):
    """
    计算数字的平方根
    
    参数:
    - number: 非负数
    
    返回:
    - 数字的平方根
    """
    if number < 0:
        raise ValueError("输入必须是非负数")
    return math.sqrt(number)


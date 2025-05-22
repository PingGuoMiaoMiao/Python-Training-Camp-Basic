def check_grade(score):
    """
    根据分数返回等级
    
    参数:
    - score: 学生分数，0-100的整数
    
    返回:
    - 对应的等级：优秀、良好、中等、及格、不及格
    """
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    if operation == "union":
        return set1.union(set2)
    elif operation == "intersection":
        return set1.intersection(set2)
    elif operation == "difference":
        return set1.difference(set2)
    else:
        return "无效的操作"


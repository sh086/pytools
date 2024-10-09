

def learn_list():
    # 定义列表
    list = ['数据1']
    # 显示长度
    print(len(list))
    # 追加元素,可以放不同类型的数据
    list.append(True)
    list.append(2)
    print(list)
    # 删除已有元素，若元素不存在列表中则保持
    list.remove(2)
    print(list)

def learn_number():
    print(2 * 4)
    # / 的结果必然是Double
    print(125 / 5)
    # 非 / 如果参与运算的存在双精度，则运输结果是Double
    print(1.0+1+6) # 非 / 如果参与运算的存在双精度，则运输结果是Double
    print(10-2) # 非 / 如果参与运算的不存在双精度，则运输结果是整数

def learn_str():
    str = '\t  python couRse '
    # 全部变成大写
    print(str.upper())
    # 全部变成小写
    print(str.lower())
    # 全部驼峰格式
    print(str.title())
    # 去除左边空白符
    print(str.lstrip())
    # 去除左边空白符
    print(str.rstrip())
    # 去除左右边空白符
    print(str.strip())
    # 去除前缀
    print(str.removeprefix('\t  py'))
    # 去除后缀
    print(str.removesuffix('Rse '))

    # 格式化字符
    username = '张三'
    print(f"{username} 你好")

    # 多行字符串
    line_str = """
    dddd
    dd
    """
    print(line_str)


if __name__ == '__main__':
    learn_number()







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

    # 字符串长度
    s = "Hello Word"
    print(len(s))

    # 通过索引获取单个字段
    print(s[len(s) - 1])

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

    # 打印列表中的最大值,仅可用户全部是数字的列表
    list2 = [1,2]
    print(max(list2)) # 打印列表中的最大值
    print(min(list2)) # 打印列表中的最小值
    print(sorted(list2)) # 打印排序好的列表

if __name__ == '__main__':
    # 一百万求和：for + range
    # range左闭右开
    # total = 0
    # for i in range(1,101,1):
    #     total += i
    # print(total)

    # 新建通讯录
    contacts = {"小明":123 }
    contacts['小红'] = 245
    # 判断键是否在字典中
    print("小红" in contacts)
    # 在字典中删除键值对，若不存在则报错
    del contacts['小明']
    # 查看键值对数量
    print(len(contacts))

    print(str(3)+"s")



    # .items() 返回所有键值对
    # .keys 返回所有键
    # .values 返回所有值
    for a,b in contacts.items():
        print(a,b)
        print(b)




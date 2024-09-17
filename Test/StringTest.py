
if __name__ == '__main__':
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



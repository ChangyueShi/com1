import re


def get_num(filename):
    pattern = r"\d+"  # 匹配一个或多个数字
    matches = re.findall(pattern, filename)
    if len(matches) == 1:
        return matches[0]
    else:
        return None


# print(get_num("data\\xml\\123.xml"))

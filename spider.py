import re
import requests
import random

# import signinapi
# import time


def search_video(csv_path, search_name):
    # uid = signinapi.signin()
    print(f"根据您的输入\"{search_name}\"及您的偏好，正在为您查找最符合您心意的相关视频...")
    print("正在获取视频弹幕弹幕...")
    headers = {"user-agent": "Mozilla/5.0"}
    url = "https://search.bilibili.com/all?keyword=" + search_name
    req = requests.get(url, headers=headers)
    content = req.text
    pattern = re.compile('<a href="//www.bilibili.com/video/(.*?)\?from=search" title=')
    lst_add = pattern.findall(content)
    bvs = lst_add[0:10]
    for i, bv in enumerate(bvs):
        url = "https://www.bilibili.com/video/" + bv
        res = requests.get(url)
        cid = re.findall(r'"cid":(.*?),', res.text)[1]
        # 获取cid，我们可以根据cid得到特定视频弹幕api

        url = f"https://comment.bilibili.com/{cid}.xml"
        res = requests.get(url)
        with open(f"data\\xml\\{cid}.xml", "wb") as f:
            f.write(res.content)
        # 以上是获取弹幕.xml文件
        # 保存在本地，为{cid}.xml

        with open(f"data\\xml\\{cid}.xml", encoding="utf-8") as f:
            data = f.read()
        comments = re.findall('<d p="(.*?)">(.*?)</d>', data)
        danmus = [",".join(item) for item in comments]
        headers = [
            "stime",
            "mode",
            "size",
            "color",
            "date",
            "pool",
            "author",
            "dbid",
            "text",
        ]
        headers = ",".join(headers)
        danmus.insert(0, headers)
        # 进行弹幕数据清洗，并将其各个部分转化为表格数据集，表格头分别为'stime', 'mode', 'size', 'color', 'date', 'pool', 'author', 'dbid', 'text'
        # 以便后续数据分析。保存在本地，命名为：danmus.csv
        csv_file = f"{csv_path}\\danmus_{i+1}.csv"

        with open(csv_file, "w", encoding="utf_8_sig") as f:
            f.writelines([line + "\n" for line in danmus])
        # 规定读取文件格式，防止乱码
        print(f"共找到{len(comments)}条弹幕")
    rcmdnum = random.randint(0, 9)
    rcmdurl = f"https://www.bilibili.com/video/{bvs[rcmdnum]}"
    return rcmdurl


# search_video("data/csv")

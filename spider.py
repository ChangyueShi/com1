# import re
# import requests
# import random
#
# # import signinapi
# # import time
#
#
# def search_video(csv_path):
#     # uid = signinapi.signin()
#     search_name = input("请输入查找视频的名称: ")
#     print("根据您的输入及您的uid，正在为您查找最符合您心意的相关视频...")
#     print("正在获取视频弹幕弹幕...")
#     headers = {"user-agent": "Mozilla/5.0"}
#     url = "https://search.bilibili.com/all?keyword=" + search_name
#     req = requests.get(url, headers=headers)
#     content = req.text
#     pattern = re.compile('<a href="//www.bilibili.com/video/(.*?)\?from=search" title=')
#     lst_add = pattern.findall(content)
#     bvs = lst_add[0:10]
#     for i, bv in enumerate(bvs):
#         url = "https://www.bilibili.com/video/" + bv
#         res = requests.get(url)
#         cid = re.findall(r'"cid":(.*?),', res.text)[1]
#         # 获取cid，我们可以根据cid得到特定视频弹幕api
#
#         url = f"https://comment.bilibili.com/{cid}.xml"
#         res = requests.get(url)
#         with open(f"data\\xml\\{cid}.xml", "wb") as f:
#             f.write(res.content)
#         # 以上是获取弹幕.xml文件
#         # 保存在本地，为{cid}.xml
#
#         with open(f"data\\xml\\{cid}.xml", encoding="utf-8") as f:
#             data = f.read()
#         comments = re.findall('<d p="(.*?)">(.*?)</d>', data)
#         danmus = [",".join(item) for item in comments]
#         headers = [
#             "stime",
#             "mode",
#             "size",
#             "color",
#             "date",
#             "pool",
#             "author",
#             "dbid",
#             "text",
#         ]
#         headers = ",".join(headers)
#         danmus.insert(0, headers)
#         # 进行弹幕数据清洗，并将其各个部分转化为表格数据集，表格头分别为'stime', 'mode', 'size', 'color', 'date', 'pool', 'author', 'dbid', 'text'
#         # 以便后续数据分析。保存在本地，命名为：danmus.csv
#         csv_file = f"{csv_path}\\danmus_{i+1}.csv"
#
#         with open(csv_file, "w", encoding="utf_8_sig") as f:
#             f.writelines([line + "\n" for line in danmus])
#         # 规定读取文件格式，防止乱码
#         print(f"共找到{len(comments)}条弹幕")
#     rcmdnum = random.randint(0, 9)
#     rcmdurl = f"https://www.bilibili.com/video/{bvs[rcmdnum]}"
#     return rcmdurl
#
#
# # search_video("data/csv")
import re
import requests
import random


def search_video(search_name):
    csv_path ="data/csv"
    print("根据您的输入正在为您查找最符合您心意的相关视频...")
    print("正在获取视频弹幕弹幕...")
    headers = {"user-agent": "Mozilla/5.0"}
    url = "https://search.bilibili.com/all?keyword=" + search_name
    req = requests.get(url, headers=headers)
    content = req.text
    pattern = re.compile('<a href="//www.bilibili.com/video/(.*?)\?from=search" title=')
    lst_add = pattern.findall(content)
    bvs = lst_add[0:5]
    for i, bv in enumerate(bvs):
        url = "https://www.bilibili.com/video/" + bv
        res = requests.get(url)
        cid = re.findall(r'"cid":(.*?),', res.text)[1]


        # view_num = re.findall(pattern2,res.text)[-1]
        # print(view_num)
        #
        # author = re.findall(r'<meta itemprop="author" content="(.*?)">', res.text)[1]

        # 获取弹幕
        url = f"https://comment.bilibili.com/{cid}.xml"
        res = requests.get(url)
        with open(f"data\\xml\\{cid}.xml", "wb") as f:
            f.write(res.content)

        with open(f"data\\xml\\{cid}.xml", encoding="utf-8") as f:
            data = f.read()
        comments = re.findall('<d p="(.*?)">(.*?)</d>', data)
        danmus = [",".join(item) for item in comments]

        # 存取视频信息

        csv_vidoe_file = f"{csv_path}\\video.csv"
        with open(csv_vidoe_file, "w", encoding="utf_8_sig") as f:
            f.writelines([line + "\n" for line in danmus])

        # 存取弹幕信息
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

        csv_file = f"{csv_path}\\danmus_{i + 1}.csv"
        #
        with open(csv_file, "w", encoding="utf_8_sig") as f:
            f.writelines([line + "\n" for line in danmus])
            print(f"共找到{len(comments)}条弹幕")
        # rcmdnum = random.randint(0, 9)
        # rcmdurl = f"https://www.bilibili.com/video/{bvs[rcmdnum]}"
        # # 保存弹幕及视频信息到文件
        # csv_file = f"{csv_path}\\danmus_{i + 1}.csv"
        # with open(csv_file, "w", encoding="utf_8_sig") as f:
        #     f.write(f"视频标题: {title}\n")
        #     #
        #     # f.write(f"作者名: {author}\n")
        #     f.writelines([line + "\n" for line in danmus])
        #
        # print(f"共找到{len(comments)}条弹幕")
        # print(f"视频标题: {title}")
        # # print(f"作者名: {author}")

    rcmdnum = random.randint(0, 4)
    rcmdurl = f"https://www.bilibili.com/video/{bvs[rcmdnum]}"

    return csv_file


# search_video("data/csv")
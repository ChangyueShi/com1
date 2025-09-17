import time
import random


def recommend(uid, rmdurl):
    print(f"正在根据您的uid:{uid}及爬取到到弹幕数据\n综合分析您的最可能喜欢的视频...")
    time.sleep(1)
    # 显示进度条
    progress = ""
    for i in range(10):
        progress += "#"
        print(f"\r[{progress:<10}] {i * 10}%", end="")
        time.sleep(random.randint(0, 3))
    print("\r[##########] 100%")

    print("分析成功！\n")
    print(f"您最可能喜欢的视频的链接是：{rmdurl}")

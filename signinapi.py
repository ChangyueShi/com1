import time
import random


def signin(uid):
    print(f"您输入的uid号: {uid}")
    print("正在获取偏好数据，请稍候...")
    time.sleep(1)

    # 显示进度条
    progress = ""
    for i in range(10):
        progress += "#"
        print(f"\r[{progress:<10}] {i * 10}%", end="")
        time.sleep(random.randrange(0, 2))
    print("\r[##########] 100%")

    print("获取偏好数据成功！")
    # return uid

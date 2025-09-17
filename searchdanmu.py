import re

def searchdanmu(csv_path):
    with open(csv_path, encoding='utf-8') as f:
        danmus = []
        for line in f.readlines()[1:]:
            time = int(float(line.split(',')[0]))
            text = line.split(',')[-1].replace('\n', '')
            danmus.append([time, text])
    # 从数据集中提取关键所需数据。

        danmus.sort(key=lambda x: x[0])
    danmu = input("请输入要查找的弹幕: ")
    dictt1 = {}
    dictt2 = {}
    control = True
    for item in danmus:
        if re.search(danmu, item[1]):
            print(f'{int(item[0] / 60)}m{item[0] % 60}s {item[1]}')
            control = False
            continue
        if danmu in item[1]:
            minute = int(item[0] / 60)
            second = item[0] % 60
            dictt1[minute] = dictt1.get(minute, 0) + 1
            dictt2[minute] = dictt2.get(minute, 0) + second
        else:
            pass

    if control:
        print('没有找到包含"' + danmu +'"的弹幕')
    # 查找视频名场面。

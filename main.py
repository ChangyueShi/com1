import spider
import visualization
import signinapi
import EPT_recmdAlgo
import tkinter as tk
from tkinter import ttk
# import searchdanmu


csv_path = "data/csv"


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('bilibili弹幕分析和推荐')
        self.root.geometry("570x400")
        self.interface()

    def interface(self):
        self.Label0 = tk.Label(self.root, text="bilibili弹幕分析和视频推荐")
        self.Label0.grid(row=0, column=0)
        self.Label1 = tk.Label(self.root, text="输入自己uid：")
        self.Label1.grid(row=1, column=0)
        self.entry00 = tk.StringVar()
        self.Entry0 = tk.Entry(self.root, textvariable=self.entry00)
        self.Entry0.grid(row=2, column=0)
        self.Label2 = tk.Label(self.root, text="输入搜索名称：")
        self.Label2.grid(row=3, column=0)
        self.entry10 = tk.StringVar()
        self.Entry1 = tk.Entry(self.root, textvariable=self.entry10)
        self.Entry1.grid(row=4, column=0)
        self.Label3 = tk.Label(self.root, text="选择词云样式预设：")
        self.Label3.grid(row=5, column=0)
        values = ['⚪', '♥', '💎', '🔺', '▲', '⭐']
        self.combobox0 = tk.StringVar()
        self.combobox = ttk.Combobox(
            master=self.root,
            height=6,
            width=20,
            state='readonly',
            cursor='arrow',
            font=('', 15),
            textvariable=self.combobox0,
            values=values, 
            )
        self.combobox.grid(padx=150)
        self.Button0 = tk.Button(self.root, text="确认", command=self.event)
        self.Button0.grid(row=7, column=0)
        self.w1 = tk.Text(self.root, width=80, height=10)
        self.w1.grid(row=8, column=0)

    def event(self):
        uid = self.entry00.get()
        search_name = self.entry10.get()
        dict = {'⚪': 1, '♥': 2, '💎': 3, '🔺': 4, '▲': 5, '⭐': 6}
        ciyun_code = self.combobox0.get()
        signinapi.signin(uid)
        rcmdurl = spider.search_video(csv_path, search_name)
        print("正在对爬取到的数据进行数据分析...")
        for i in range(1, 11):
            visualization.hightlights(f"{csv_path}/danmus_{i}.csv")
            visualization.emotionAnalysis(f"{csv_path}/danmus_{i}.csv")
            visualization.wordCloud(f"{csv_path}/danmus_{i}.csv", shapeofall=dict[ciyun_code])
        EPT_recmdAlgo.recommend(uid, rcmdurl)
        self.w1.insert("insert", f"您最可能喜欢的视频的链接是：{rcmdurl}")


if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()

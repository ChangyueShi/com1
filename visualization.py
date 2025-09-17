from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line
from pyecharts import options as opts
from snownlp import SnowNLP
from pyecharts.charts import Pie
import jieba
from pyecharts.charts import WordCloud
import getnum


def hightlights(csv_path):
    number = getnum.get_num(csv_path)
    with open(csv_path, encoding="utf-8") as f:
        text = [float(line.split(",")[0]) for line in f.readlines()[1:]]
    text = sorted([int(item) for item in text])
    data = {}
    for item in text:
        item = int(item / 60)
        data[item] = data.get(item, 0) + 1

    x_data = list(data.keys())
    y_data = list(data.values())
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
    )
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
    )

    c = (
        Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="弹幕数量",
            y_axis=y_data,
            is_smooth=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#fff"),
            label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
            itemstyle_opts=opts.ItemStyleOpts(color="red", border_color="#fff", border_width=3),
            tooltip_opts=opts.TooltipOpts(is_show=True),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="",
                pos_bottom="5%",
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                position="left",
                axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
        )
        .render(f"data\\hlt\\highlights_{number}.html")
    )


# 根据视频中单位时间弹幕数量制作视频高光表格，并保存为超文本标记语言格式文件。保存在本地，命名为highlights.html


def emotionAnalysis(csv_path):
    number = getnum.get_num(csv_path)
    with open(csv_path, encoding="utf-8") as f:
        text = [line.split(",")[-1] for line in f.readlines()[1:]]
    # 继续分离出所需弹幕数据集

    emotions = {"正面": 0, "负面": 0, "中性": 0}
    # 定义情绪，负面，正面，中性

    for item in text:
        if SnowNLP(item).sentiments > 0.6:
            emotions["正面"] += 1
        elif SnowNLP(item).sentiments < 0.4:
            emotions["负面"] += 1
        else:
            emotions["中性"] += 1
    print(emotions)
    # 调用SnowNLP库函数计算弹幕情感倾向

    c = (
        Pie()
        .add("", list(emotions.items()))
        .set_colors(["blue", "purple", "orange"])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
        .render(f"data\\emo\\emotionAnalysis_{number}.html")
    )
    # 根据情感倾向制作饼状图，并保存为emotionAnalysis.html文件，保存在本地


def wordCloud(csv_path, shapeofall):
    number = getnum.get_num(csv_path)
    with open(csv_path, encoding="utf-8") as f:
        text = " ".join([line.split(",")[-1] for line in f.readlines()])
    # 以规定格式读取弹幕文件，并提取所需数据集。

    words = jieba.cut(text)
    # 调用结巴分词库，进行分词。

    _dict = {}
    for word in words:
        if len(word) >= 2:
            _dict[word] = _dict.get(word, 0) + 1
    items = list(_dict.items())
    items.sort(key=lambda x: x[1], reverse=True)
    shape_of_all = int(shapeofall)
    # code = int(input("选择词云样式预设：\n1.⚪\n2.♥\n3.💎\n4.🔺\n5.▲\n6.⭐\n"))
    c = (
        WordCloud()
        .add(
            "",
            items,
            word_size_range=[5, 60],
            shape=str(shape_slct(shape_of_all)),
            textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
        )
        .render(f"data//wdcld//WordCloud_{number}.html")
    )


def shape_slct(number):
    if number == 1:
        return "circle"
    if number == 2:
        return "cardioid"
    if number == 3:
        return "diamond"
    if number == 4:
        return "triangle-forward"
    if number == 5:
        return "triangle"
    if number == 6:
        return "star"
    return None

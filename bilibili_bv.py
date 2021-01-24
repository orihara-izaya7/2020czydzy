from bilibili_api import video
import re
import pandas as pd

# BVid、fileName
BVid = input("输入BV号")
# 获取弹幕
my_video = video.get_video_info(bvid=BVid)

file_name = BVid+'.csv'
danmu=video.get_danmaku(bvid=BVid)
data = [data.text for data in danmu]
for i in data:
    i = re.sub('\s+', '', i)

print("弹幕数量为：{}".format(len(data)))

df = pd.DataFrame(data)
df.to_csv(file_name, index=False, header=None, encoding="utf_8_sig")
print("写入文件成功")
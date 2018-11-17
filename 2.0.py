from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
###当前文件路径
d = path.dirname(__file__)
file = open(path.join(d, "D:/test.txt")).read()

##进行分词
#刚开始是分完词放进txt再打开却总是显示不出中文很奇怪
default_mode =jieba.cut(file)
text = " ".join(default_mode)

# 图片
alice_mask = np.array(Image.open(path.join(d, "D:/qq.jpg")))


stopwords = set(STOPWORDS)
stopwords.add("said")
fontname = path.join(d, 'C:/Windows/Fonts/SimSun-ExtB.ttf')
wc = WordCloud(  
    #设置字体，不指定就会出现乱码,这个字体文件需要下载
    #font_path = fontname,  
    background_color="white",   
    max_words=2000,   
    mask=alice_mask,  
    stopwords=stopwords)  
wc.generate(text)

image_colors = ImageColorGenerator(alice_mask)
# store to file
wc.to_file(path.join(d, "D:/qq_result.jpg"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
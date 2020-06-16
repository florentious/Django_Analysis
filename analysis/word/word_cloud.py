from wordcloud import WordCloud
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np

import os
import time

from analysis.utils.option import Options

opt = Options()


def img_wordcloud(keywords, font_path=opt.font_path, backgound_color=opt.background_color):
    wordcloud = WordCloud(
        font_path        = font_path      ,
        width            = 400            ,
        height           = 400            ,
        background_color = backgound_color
    )

    wordcloud = wordcloud.generate_from_frequencies(keywords)
    img_array = wordcloud.to_array()

    fig = plt.figure(figsize=(10, 10))
    plt.imshow(img_array, interpolation="bilinear")
    plt.axis("off")

    # today_path before current path
    today = str(time.gmtime(time.time()).tm_mday)
    today_path = 'polls/static/img/' + today + '/'
    if not os.path.exists(today_path):
        os.mkdir(today_path)

    cur_time = str(round(time.time()*1000000))
    img_path = today_path + cur_time + '.png'
    fig.savefig(img_path)

    res_path = '../../../static/img/' + today + '/' + cur_time + '.png'

    return res_path

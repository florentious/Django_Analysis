"""
    maker = Florentious



"""

from analysis.utils.option import Options
from analysis.word.word_cloud import img_wordcloud

from collections import defaultdict
from konlpy.tag import Okt



opt = Options()


# get stop_word list
def get_stopword(path=opt.stop_word, enc='utf-8'):
    with open(path, encoding=enc) as f:
        tmp_lines = f.readlines()
        stop_word = [x.strip() for x in tmp_lines]
    return stop_word


# pop stop_word by dictionary
# input  : dictionary, (stop_word file path)
# output : removed stop_word dictionary
def pop_stopword(input_dict, additional_stop_word=None, stopword_path=opt.stop_word, enc='utf-8'):
    if additional_stop_word is None:
        additional_stop_word = []

    stop_word = get_stopword(stopword_path, enc)
    stop_word.extend(additional_stop_word)

    for word in stop_word:
        if word in input_dict:
            input_dict.pop(word)

    return input_dict


# sorted reverse(maxcount)
def auto_sorted(lv_input_dict, count=opt.max_count):

    return sorted(lv_input_dict.items(), key=lambda item: item[1], reverse=True)[:count]


# get keyword dictionary
def get_worddictionary(input_, additional_stop_word=None, stopword_path=opt.stop_word, enc='utf-8', count=opt.max_count):
    if additional_stop_word is None:
        additional_stop_word = []

    word_dict = defaultdict(int)
    tmp_nouns = Okt().nouns(input_)

    if tmp_nouns :
        for word in tmp_nouns:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    tmp_dict = pop_stopword(word_dict,additional_stop_word=additional_stop_word,stopword_path=stopword_path, enc=enc)
    cloud_path = img_wordcloud(keywords=tmp_dict)

    return (auto_sorted(tmp_dict, count=count), cloud_path)


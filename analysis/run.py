# from analysis.utils.option import Options
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Okt
# import pymysql
# import sqlalchemy
# import os
# from collections import defaultdict

# from analysis.word.word_dictionary import get_worddictionary

# opt = Options()

# print(opt.stop_word)
# print(Okt().pos('텍스트 테스트 '))

input_text = '지금과 고통'

path = 'data/test_data/'
#
# txt_list = os.listdir(path)
# tmp_data = ""
#
# # txt to sentences
# for txt in txt_list:
#     with open(path + txt, encoding='utf-8') as f:
#         tmp = f.read()
#         tmp_data = tmp_data + tmp + '\n'
#
# wordDict = get_worddictionary(tmp_data)
# print(wordDict)

# print(get_worddictionary(input_text))

print(Okt().pos(input_text))
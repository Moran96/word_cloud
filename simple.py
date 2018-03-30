#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
text_from_file_with_apath = open('/Users/a/Desktop/sta2.2/Python/result.txt').read()
 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
 
my_wordcloud = WordCloud().generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()


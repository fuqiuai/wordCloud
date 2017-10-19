# coding:utf-8

from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    #  text = open(path.join(d, 'doc//十九大报告全文.txt')).read()
    text = open(path.join(d,'doc//alice.txt')).read()
    #  text="付求爱很帅并来到付求爱了网易研行大厦很帅 很帅 很帅"

    # 若是中文文本，则先进行分词操作
    text=chnSegment.word_segment(text)
    
    # 生成词云
    plotWordcloud.generate_wordcloud(text)

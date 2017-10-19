# wordCloud
用python进行文本分词并生成词云

## 需要安装的包
* `sudo pip3 install jieba`
* `sudo pip3 install wordcloud`
* wordcloud包依赖于Pillow，numpy，matplotlib 

## 其他
* 分词采用结巴分词，并支持自定义字典
* 分词结果进行词频统计分析，并导出
* 词云图可自己设定背景图（英文词云图不需先进行分词）

## 运行结果
运行demo.py,会生成“2017年中央政府工作报告(全文).txt”的词云图，和“词频统计.txt”  
词云图如下：  
![image](https://raw.githubusercontent.com/fuqiuai/wordCloud/master/Images/alice.png)



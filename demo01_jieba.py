# coding:utf-8
import jieba
import jieba.posseg as psg

print(type(jieba))
content = '提升睡眠质量的核心是建立规律且稳定的睡眠节律，同时优化睡前状态与睡眠环境，以下是分维度的具体习惯，兼顾科学性和可操作性，这里有一家上市公司'


# jieba实现精确模式的分词
def dm1_jieba():
    # 1. 给出需要待切分的文本
    # 2. 基于jieba.cut()方法实现文本的切分
    result1 = jieba.cut(content, cut_all=False)  # 返回时生成器：for循环、next()、强制类型转换：list
    print(f'result1 -> {result1}')
    # print(next(result1))  # for循环底层也是通过next()方法取出的
    # for value in result1:
    #     print(value)
    print(list(result1))
    # 3. 基于jieba.lcut()方法实现文本的切分
    result2 = jieba.lcut(content, cut_all=False)
    print(result2)


# jieba实现全模式的分词
def dm2_jieba():
    # 1. 给出需要待切分的文本

    # 2. 基于jieba.cut()方法实现文本的切分
    # result1 = jieba.cut(content, cut_all=True) # 返回时生成器：for循环、next()、强制类型转换：list
    # print(f'result1 -> {result1}')
    # # print(next(result1))  # for循环底层也是通过next()方法取出的
    # # for value in result1:
    # #     print(value)
    # print(list(result1))
    # 3. 基于jieba.lcut()方法实现文本的切分
    result2 = jieba.lcut(content, cut_all=True)
    print(result2)


# jieba实现搜索引擎的分词
def dm3_jieba():
    # 1. 给出需要待切分的文本

    # 3. 基于jieba.lcut()方法实现文本的切分，精确模式上对长文本再次切分
    result2 = jieba.lcut_for_search(content)
    print(result2)


# jieba支持中文繁体
def dm4_jieba():
    print(jieba.lcut('煩惱即是菩薩，我暫時不提'))


# jieba支持自定义词典，需要考虑词频 word freq speech
def dm5_jieba():
    # 加载自定义词典
    jieba.load_userdict('./userdict.txt')  # 调整“上市”的词频，观察分词结果
    print(jieba.lcut(content))

def dm6_jieba():
    # 1. 给出需要待切分的文本

    # 3. 基于jieba.lcut()方法实现文本的切分，精确模式上对长文本再次切分
    result2 = psg.lcut(content)
    print(result2)


# 鲁迅，浙江绍兴人，五四新文化运动的重要参与者，代表作朝花夕拾

if __name__ == '__main__':
    dm1_jieba()
    dm2_jieba()
    dm3_jieba()
    dm4_jieba()
    dm5_jieba()
    dm6_jieba()

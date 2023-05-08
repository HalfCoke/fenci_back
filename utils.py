import jieba
from collections import Counter


def jieba_cut(text):
    with open('data/stop.txt', encoding='utf-8') as f:
        stop_word = []
        line = f.readline()
        while line:
            stop_word.append(line.strip())
            line = f.readline()
    with open('data/cus_stop.txt', encoding='utf-8') as f:
        cus_stop_word = []
        line = f.readline()
        while line:
            cus_stop_word.append(line.strip())
            line = f.readline()
    with open('data/cus.txt', encoding='utf-8') as f:
        cus_word = []
        line = f.readline()
        while line:
            stop_word.append(line.strip())
            line = f.readline()
    jieba.load_userdict(cus_word)
    # 使用结巴分词将文本分成单词，并去除停用词
    tokens = [token for token in jieba.cut_for_search(text) if
              token not in [' ', '\n', '\r\n'] and token not in stop_word and token not in cus_stop_word and len(
                  token) > 0]

    # 统计单词频率
    freqs = Counter(tokens)

    # 打印前10个最常见的单词
    res = [f'{item[0]}:{item[1]}' for item in freqs.most_common(100)]
    return res

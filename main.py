from utils import jieba_cut

if __name__ == '__main__':
    # 读取文本文件
    with open('1.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    print('\n'.join(jieba_cut(text)))

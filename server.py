import jieba
from flask import Flask, request

from utils import jieba_cut

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        content = file.read().decode('utf-8')
        # 在这里处理文件内容
        return '<br>'.join(jieba_cut(content))
    return '''
        <html>
            <body>
                <form action="/" method="post" enctype="multipart/form-data">
                    <input type="file" name="file">
                    <input type="submit" value="上传文件">
                </form>
            </body>
        </html>
    '''


@app.route('/word/<word>', methods=['GET'])
def edit_dict(word):
    if str(word).startswith('-'):
        with open('data/cus_stop.txt', 'a', encoding='utf-8') as f:
            f.write(str(word).lstrip('-'))
            f.write('\n')
        return '已增加停用词：' + str(word).lstrip('-')
    with open('data/cus.txt', 'a', encoding='utf-8') as f:
        f.write(str(word))
        f.write('\n')
    jieba.add_word(word)
    return '已添加自定义词组：' + word


@app.route('/get_stop', methods=['GET'])
def get_stop():
    with open('data/cus_stop.txt', encoding='utf-8') as f:
        cus_stop_word = []
        line = f.readline()
        while line:
            cus_stop_word.append(line.strip())
            line = f.readline()
    return '<h1>停用词组</h1><br>' + '<br>'.join(cus_stop_word)


@app.route('/get_cus', methods=['GET'])
def get_cus():
    with open('data/cus.txt', 'r', encoding='utf-8') as f:
        cus_word = []
        line = f.readline()
        while line:
            cus_word.append(line.strip())
            line = f.readline()
    return '<h1>自定义词组</h1><br>' + '<br>'.join(cus_word)


@app.route('/reset_stop', methods=['GET'])
def reset_stop():
    with open('data/cus_stop.txt', 'w', encoding='utf-8') as f:
        f.write('')
    return '重置停用词'


@app.route('/reset', methods=['GET'])
def reset_cus():
    with open('data/cus.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            jieba.del_word(line)
            line = f.readline()
    with open('data/cus.txt', 'w', encoding='utf-8') as f:
        f.write('')
    return '重置自定义词组'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)

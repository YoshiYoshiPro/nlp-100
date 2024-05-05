# !apt-get install mecab libmecab-dev mecab-ipadic-utf8
# !pip install mecab-python3 japanize-matplotlib

import os

os.environ['MECABRC'] = '/etc/mecabrc'

import MeCab

# MeCab インスタンスの初期化（辞書のパスを明示的に指定）
mecab = MeCab.Tagger('-r /etc/mecabrc')

# 形態素解析を行いたいテキストファイルを読み込む
with open('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()

# 形態素解析を実行
parsed_text = mecab.parse(original_text)

# 結果をファイルに保存
with open('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab', 'w', encoding='utf-8') as file:
    file.write(parsed_text)

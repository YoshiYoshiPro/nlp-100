# 24. ファイル参照の抽出
import re

"""
[[ファイル:Royal Coat of Arms of the United Kingdom.svg|thumb|イギリスの国章]]
[[File:Descriptio Prime Tabulae Europae.jpg|thumb|left|フランチェスコ・ロッセリの地図「ヨーロッパ表」]]
"""

# 正規表現パターン
# ファイル|File :「ファイル」または「File」のいずれかにマッチ
# [ ] :文字クラスの定義。文字クラス内で指定された任意の1文字にマッチ
# ^ :文字クラスの冒頭に置かれると否定の意味を持つ
# | :通常は選択(OR)を意味するが、文字クラス内で使用されているので、単純にパイプ文字自体を指す
# [^] :括弧内に指定されたどの文字にもマッチしない一文字
# [^]|] :「]」と「|」にもマッチしない一文字
# + :直前の文字（またはパターン）が1回以上、無限回まで繰り返しマッチ
# ([^]|]+) :「]」または「|」が登場するまでの1文字以上の任意の文字列にマッチ
pattern = r'\[\[(ファイル|File):([^]|]+)'

files = re.findall(pattern, article['text'])

for file in files:
  print(file[1])    #file[1]は2番目のキャプチャグループを指す

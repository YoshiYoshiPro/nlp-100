# 23. セクション構造
import re

"""
== セクション名 ==
=== セクション名 ===
==== セクション名 ====
"""

# 正規表現パターン
# {2,} :直前の文字やパターンが2回以上連続して出現（{n,m} :nは繰り返しの最小回数、mは最大回数を指定）
# \s :空白文字にマッチ（スペース、タブ、改行、復帰、フォームフィード、垂直タブが含まれる）
# \1 :最初にキャプチャしたグループ（等号の並び）と同じものを参照
pattern = r'(={2,})\s*(.*?)\s*\1'

sections = re.findall(pattern, article['text'])

for section in sections:
  level = len(section[0]) -1  #section[0]は最初のキャプチャグループを指す（== or ===など）
  section_name = section[1]   #section[1]は2番目のキャプチャグループを指す（セクション名）
  print(f'レベル{level}: {section_name}')

# 22. カテゴリ名の抽出
import re

"""
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
"""

# 正規表現パターン
# () :キャプチャグループ。マッチしたテキストを記憶することができ、参照できる。
# (?:)は非キャプチャグループとして認識される。（グループ化はされるが記憶されない）
# ?(1個目) :できるだけ少ない繰り返し回数でマッチング（最小マッチング）
# ?(2個目) :直前の要素が0回または1回出現する場合。
pattern = r'\[\[Category:(.*?)(?:\|.*?)?\]\]'

categories = re.findall(pattern, article['text'])

for category in categories:
    print(category)

# 25. テンプレートの抽出
import re

"""
{{基礎情報 国
|略名 =イギリス
|日本語国名 =グレートブリテン及び北アイルランド連合王国
|公式国名 ={{lang|en|United Kingdom of Great Britain and Northern Ireland}}
|国旗画像 =Flag of the United Kingdom.svg
...（略）...
}}
"""

# "基礎情報"から"<references/>"までの間にある任意の文字列にマッチ
pattern = '基礎情報(.*?\<references/\>)'
result = re.findall(pattern, article['text'], re.DOTALL)    # re.DOTALL :「.」が改行文字（\n）を含むあらゆる単一文字にマッチ（基礎情報内のテキストが改行されているため。）

result[0] += "\n"   # resultは要素1つのみのリスト。末尾に改行文字を追加。
# (?<=\n\|) :直前に改行文字と縦棒（|）があることを確認。（肯定的後読みアサーション）
# (?=\n) :直後に改行文字があることを確認。（肯定的先読みアサーション）
pattern = '(?<=\n\|)(.*?)\s*=\s*(.*?)(?=\n)'
result2 = re.findall(pattern, result[0])

info_dict = {}
for key, value in result2:
    info_dict[key] = value.strip()    # strip() :文字列の両端（先頭と末尾）から指定した文字（デフォルトでは空白文字）を削除

print(info_dict)

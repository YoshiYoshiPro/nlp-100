# 27. 内部リンクの除去
import re


# MediaWikiの内部リンクマークアップを除去する関数
def remove_internal_links(text):
    # (?:[^|]*?\|)*? :「|」記号までの任意の文字列を非キャプチャグループとしてマッチ。リンクの表示テキストと実際のリンク先を区切る「|」記号までの部分がマッチ
    # ([^|]*?) :「|」記号から「]]」までの部分をキャプチャグループとしてマッチ。
    pattern = r'\[\[(?:[^|]*?\|)*?([^|]*?)\]\]'
    return re.sub(pattern, r'\1', text)   # マッチした内部リンク全体をキャプチャした部分に置換

info_dict3 = {}
for key, text in info_dict2.items():
    text = remove_internal_links(text)
    info_dict3[key] = text

print(info_dict3)

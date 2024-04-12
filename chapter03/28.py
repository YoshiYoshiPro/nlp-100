# 28. MediaWikiマークアップの除去
import re


def remove_markup(text):
    patterns = [
        r"'{2,5}",  # 強調マークアップ
        r'\[\[(?:[^|]*?\|)*?([^|]*?)\]\]',  # 内部リンク
        r'\[(?:https?://|//?)[^\s]*?\s([^]]*?)\]',  # 外部リンク
        r'\{\{.*?\}\}',  # テンプレート
        r'<ref.*?</ref>',  # 参照
        r'<!--.*?-->',  # コメント
    ]

    for pattern in patterns:
        text = re.sub(pattern, '', text, flags=re.DOTALL)

    return text.strip()

pattern = '基礎情報(.*?\<references/\>)'
result = re.findall(pattern, article['text'], re.DOTALL)

result[0] += "\n"
pattern = '(?<=\n\|)(.*?)\s*=\s*(.*?)(?=\n)'
result2 = re.findall(pattern, result[0])

info_dict2 = {key: remove_markup(value) for key, value in result2}

# print(info_dict2)
for key, value in info_dict.items():
    print(f"{key}: {value}")

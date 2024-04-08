# 元の文
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# 句読点を除去
text = text.replace(',', '').replace('.', '')
# 単語に分割
words = text.split()
# 各単語のアルファベットの文字数（リスト内包表記）
word_lengths = [len(word) for word in words]

print(word_lengths)

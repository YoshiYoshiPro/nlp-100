text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# 句読点を除去し、単語に分割
words = text.replace('.', '').split()
# 先頭の1文字を取り出す単語のインデックス
one_letter_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
# 単語の位置（先頭から何番目の単語か）への連想配列（辞書型）
word_positions = {words[i][:1] if (i + 1) in one_letter_positions else words[i][:2]: i + 1 for i in range(len(words))}

# 結果を表示
print(word_positions)

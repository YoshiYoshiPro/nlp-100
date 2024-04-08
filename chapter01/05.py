def n_gram(sequence, n):
    n_grams = [sequence[i:i+n] for i in range(len(sequence)-n+1)]
    return n_grams


text = "I am an NLPer"
words = text.split()

# 単語bi-gramを生成
word_bi_gram = n_gram(words, 2)

# 文字bi-gramを生成（スペースも含む）
char_bi_gram = n_gram(text, 2)

print(word_bi_gram)
print(char_bi_gram)

# 35. 単語の出現頻度
from collections import defaultdict


def calculate_word_frequency(sentences):
    word_frequency = defaultdict(int)
    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] != '記号':
                word_frequency[morph['base']] += 1
    return sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
word_freq = calculate_word_frequency(sentences)
print(f"単語の出現頻度上位10件: {word_freq[:10]}")

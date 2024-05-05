# 38. ヒストグラム
from collections import defaultdict

import matplotlib.pyplot as plt


def calculate_word_frequency(sentences):
    word_frequency = defaultdict(int)
    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] != '記号':
                word_frequency[morph['base']] += 1
    return word_frequency

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
word_freq = calculate_word_frequency(sentences)

freq_counts = defaultdict(int)
for freq in word_freq.values():
    freq_counts[freq] += 1

freqs = list(freq_counts.keys())
counts = list(freq_counts.values())

plt.figure(figsize=(10, 6))
plt.hist(list(word_freq.values()), bins=100, range=(1, 100))
plt.title('単語の出現頻度のヒストグラム')
plt.xlabel('出現頻度')
plt.ylabel('単語の異なり数')
plt.xlim(1, 100)
plt.tight_layout()
plt.show()

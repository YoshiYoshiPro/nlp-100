# 36. 頻度上位10語
import japanize_matplotlib
import matplotlib.pyplot as plt


def calculate_word_frequency(sentences):
    word_frequency = defaultdict(int)
    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] != '記号':
                word_frequency[morph['base']] += 1
    return sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
word_freq = calculate_word_frequency(sentences)

top_words = [word for word, freq in word_freq[:10]]
top_freqs = [freq for word, freq in word_freq[:10]]

plt.figure(figsize=(10, 6))
plt.bar(top_words, top_freqs)
plt.title('出現頻度上位10語')
plt.xlabel('単語')
plt.ylabel('出現頻度')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 34. 名詞の連接
def extract_longest_noun_sequence(sentences):
    longest_noun_sequences = []
    for sentence in sentences:
        noun_sequence = []
        for morph in sentence:
            if morph['pos'] == '名詞':
                noun_sequence.append(morph['surface'])
            else:
                if len(noun_sequence) > 1:
                    longest_noun_sequences.append("".join(noun_sequence))
                noun_sequence = []
        if len(noun_sequence) > 1:
            longest_noun_sequences.append("".join(noun_sequence))
    return longest_noun_sequences

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
longest_noun_sequences = extract_longest_noun_sequence(sentences)
print(f"最長の名詞の連接の数: {len(longest_noun_sequences)}")
print(f"最初の10個の最長の名詞の連接: {longest_noun_sequences[:10]}")

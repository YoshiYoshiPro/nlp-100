# 32. 動詞の基本形
def extract_verb_bases(sentences):
    verb_bases = []
    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] == '動詞':
                verb_bases.append(morph['base'])
    return verb_bases

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
verb_bases = extract_verb_bases(sentences)
print(f"動詞の基本形の数: {len(verb_bases)}")
print(f"最初の10個の動詞の基本形: {verb_bases[:10]}")

# 31. 動詞
def extract_verbs(sentences):
    verbs = []
    for sentence in sentences:
        for morph in sentence:
            if morph['pos'] == '動詞':
                verbs.append(morph['surface'])
    return verbs

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
verbs = extract_verbs(sentences)
print(f"動詞の表層形の数: {len(verbs)}")
print(f"最初の10個の動詞の表層形: {verbs[:10]}")

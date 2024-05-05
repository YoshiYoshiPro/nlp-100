# 33. 「AのB」
def extract_noun_phrases(sentences):
    noun_phrases = []
    for sentence in sentences:
        for i in range(len(sentence) - 2):
            if sentence[i]['pos'] == '名詞' and sentence[i+1]['surface'] == 'の' and sentence[i+2]['pos'] == '名詞':
                noun_phrases.append(sentence[i]['surface'] + sentence[i+1]['surface'] + sentence[i+2]['surface'])
    return noun_phrases

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
noun_phrases = extract_noun_phrases(sentences)
print(f"「AのB」の形の名詞句の数: {len(noun_phrases)}")
print(f"最初の10個の「AのB」の形の名詞句: {noun_phrases[:10]}")

# 30. 形態素解析結果の読み込み
def parse_neko(mecabfile):
    with open(mecabfile, 'r', encoding='utf-8') as f:
        sentences = []
        morphemes = []
        for line in f:
            if line == 'EOS\n':
                if len(morphemes) > 0:
                    sentences.append(morphemes)
                    morphemes = []
            else:
                fields = line.split('\t')
                if len(fields) != 2 or fields[0] == '':
                    continue
                attrs = fields[1].split(',')
                morph = {
                    'surface': fields[0],
                    'base': attrs[6],
                    'pos': attrs[0],
                    'pos1': attrs[1]
                }
                morphemes.append(morph)
        return sentences

sentences = parse_neko('/content/drive/MyDrive/Colab Notebooks/nlp-100/neko.txt.mecab')
print(f"文の数: {len(sentences)}")
print(f"最初の3文の形態素情報:")
for i, sentence in enumerate(sentences[:3], start=1):
    print(f"文{i}:")
    for morph in sentence:
        print(f"\t{morph['surface']}（{morph['pos']}、{morph['pos1']}）")

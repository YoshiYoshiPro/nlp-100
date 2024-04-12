# 20. JSONデータの読み込み
import gzip
import json

file_path = 'jawiki-country.json.gz'

# 'r'：ファイルを読み取りモードで開く。（デフォルト）
# 't'：ファイルをテキストモードで開く。テキストモードでは、ファイルの内容が特定の文字エンコーディング（デフォルトではシステムのロケールに依存）に従って処理される。
with gzip.open(file_path, mode='rt', encoding='utf-8') as file:
  for row in file:
    article = json.loads(row)
    if article['title'] == 'イギリス':
      print(article['text'])
      break

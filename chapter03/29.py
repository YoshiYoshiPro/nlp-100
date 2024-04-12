# 29. 国旗画像のURLを取得する
import json
import re
import urllib

# 国旗画像の処理
flag_name = inf_dic['国旗画像']
url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:' + urllib.parse.quote(flag_name) + '&format=json&prop=imageinfo&iiprop=url'
connection = urllib.request.urlopen(urllib.request.Request(url))
response = json.loads(connection.read().decode())

pages = response['query']['pages']
page_id = list(pages.keys())[0]
flag_url = pages[page_id]['imageinfo'][0]['url']

print(flag_url)

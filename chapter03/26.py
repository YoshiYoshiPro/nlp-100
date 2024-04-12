# 26. 強調マークアップの除去
import re

info_dict2 = {}
for key, value in info_dict.items():
  info_dict2[key] = re.sub(r"'{2,5}" , "", value)
info_dict2

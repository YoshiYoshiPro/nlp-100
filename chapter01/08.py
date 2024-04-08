def cipher(text):
  # org(): Unicode数値に変換
  return ''.join(chr(219 - ord(x)) if 'a' <= x <= 'z' else x for x in text)

message = "This is a secret message."

encrypted = cipher(message)
print(f"暗号化されたメッセージ: {encrypted}")

decrypted = cipher(encrypted)
print(f"復号化されたメッセージ: {decrypted}")

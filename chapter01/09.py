import random

def shuffle_words(word):
  if len(word) <= 4:
    return word
  else:
    middle_word = list(word[1:-1])
    random.shuffle(middle_word)
    return word[0] + ''.join(middle_word) + word[-1]


def typoglycemia(text):
  words = text.split()
  shuffled = [shuffle_words(word) for word in words]
  return ' '.join(shuffled)


text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
typoglycemia = typoglycemia(text)

print(typoglycemia)

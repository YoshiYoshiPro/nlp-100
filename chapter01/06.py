s1 = "paraparaparadise"
s2 = "paragraph"

x = set(n_gram(s1, 2))
y  = set(n_gram(s2, 2))

union = x | y
intersection = x & y
difference = x - y

# 'se'がXおよびYに含まれるかを調べる
se_in_x = 'se' in x
se_in_y = 'se' in y

print("和集合:", union)
print("積集合:", intersection)
print("差集合:", difference)
print("'se' in X:", se_in_x)
print("'se' in Y:", se_in_y)

pt = input("Enter the plain text: ")
key = int(input("Enter the key: "))
res = [['0' for j in range(0, len(pt))] for j in range(0, key)]
r, c = 0, 0
temp = 1
for i in pt:
    res[r][c] = i
    c += 1
    if temp == 1:
        r += 1
        if r >= key - 1:
            temp = 0
    else:
        r -= 1
        if r <= 0:
            temp = 1
cipher = ""
for i in res:
    for j in i:
        if not j == '0':
            cipher += j
print(cipher)

res = [['0' for j in range(0, len(cipher))] for j in range(0, key)]
r, c = 0, 0
temp = 1
for i in pt:
    res[r][c] = i
    c += 1
    if temp == 1:
        r += 1
        if r >= key - 1:
            temp = 0
    else:
        r -= 1
        if r <= 0:
            temp = 1
for i in range(0, len(pt)):
    for j in range(0, key):
        if res[j][i] != '0':
            print(res[j][i], end="")

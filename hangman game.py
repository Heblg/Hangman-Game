word = list(input("word: ").lower())
while " " in word:
    word[word.index(" ")] = "-"

for pr in range(20):
    print("\n")

list = word.copy()
l = len(word)
tries = 5
i, a ,li = 0, 0, []

for i in range(l):
    if list[i] != "-":
        list[i] = "_"
    else:
        next

while list != word:
    lett = str(input("letter: "))
    for n in range(l):
        if lett == word[n]:
            list[n] = lett
            li.append(0)

    if 0 in li:
        print(" ".join(list), f'\n{tries = }\n')

    else:
        tries -= 1
        print(" ".join(list), f'\n-1 try | {tries = }\n')

    li = []
    if tries <= 0:
        break
if tries > 0:
    print("game over, you won")
else:
    print("game over, you lost")

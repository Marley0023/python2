stroka = str(input('Введите строку: '))
simvoli = []
word = ""
for char in stroka:
    if char != " ":
        word += char
    else:
        simvoli.append(word)
        word = ""
simvoli.append(word)

grouped = []
minigroup = [simvoli[0]]

for i in range(1, len(simvoli)):
    if simvoli[i] == minigroup[-1]:
        minigroup.append(simvoli[i])
    else:
        grouped.append(minigroup)
        minigroup = [simvoli[i]]
grouped.append(minigroup)
print(grouped)

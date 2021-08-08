# Translator

n = int(input())  #words in dictionary
farsi = []
english = []
french = []
germen = []

for i in range(0,n):
    fa ,en ,fr ,ge = input().split(sep=" ")
    farsi.append(fa)
    english.append(en)
    french.append(fr)
    germen.append(ge)
sentence = input()

r =  []
for i in sentence.split():
    if i in english:
        r.append(farsi[english.index(i)])
    elif i in french:
        r.append(farsi[french.index(i)])
    elif i in germen:
        r.append(farsi[germen.index(i)])
    else:
        r.append(i)

for i in r:
    print(f'{i} ', end="")


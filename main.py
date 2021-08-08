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
if sentence.split()[0] in english or sentence.split()[1] in english or sentence.split()[2] in english:
    for i in sentence.split():
        if i in english:
            r.append(farsi[english.index(i)])
        else:
            r.append(i)
elif sentence.split()[0] in french or sentence.split()[1] in french or sentence.split()[2] in french:
    for i in sentence.split():
        if i in french:
            r.append(farsi[french.index(i)])
        else:
            r.append(i)
elif sentence.split()[0] in germen or sentence.split()[1] in germen or sentence.split()[2] in germen:
    for i in sentence.split():
        if i in germen:
            r.append(farsi[germen.index(i)])
        else:
            r.append(i)
else:
    print('something is wrong')

for i in r:
    print(f'{i} ', end="")


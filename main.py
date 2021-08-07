# Translator
n = input()  #words in dictionary
farsi = []
english = []
french = []
germen = []

for i in range(0,4):
    fa ,en ,fr ,ge = input().split(sep=" ")
    farsi.append(fa)
    english.append(en)
    french.append(fr)
    germen.append(ge)
sentence = input()

#if sentence.split()[0] in english:

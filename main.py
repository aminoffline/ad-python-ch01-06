# Translator
"""
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
"""
farsi = ['man','kheili','alaghemand','barnamenevisi']
english = ['I','very', 'interested', 'programming']
french = ['je','très','intéressé','laprogrammation']
germen = ['ich' ,'sehr' ,'interessiert' ,'Programmierung']

sentence = "I am very interested in programming"
r =  []
if sentence.split()[0] in english:
    for i in sentence.split():
        if i in english:
            r.append(farsi[english.index(i)])
        else:
            r.append(i)
else:
    print('something is wrong')
for i in r:
    print(f'{i} ', end=" ")

#print(dict(enumerate(sentence.split())))
#print(dict(enumerate(english)))

import matplotlib.pyplot as plt
fin = open('words.txt')
alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphaCount = {}
x = []
y = []
for alphabet in alphabets:
    alphaCount[alphabet] = 0
    x.append(alphabet)

print(len(alphaCount))

for words in fin:
    word = words.strip()
    for letter in word:
        alphaCount[letter] = alphaCount[letter] + 1
        

for keys in alphaCount:
    y.append(alphaCount[keys])

plt.bar(x,y)
plt.xlabel('Alphabets of the English Language', fontsize = 5)
plt.ylabel('frequency', fontsize = 5)
plt.title('Occurence of English Letters in 10000 Random words')

plt.show()

print(alphaCount)


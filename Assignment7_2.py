fhand = open("romeo.txt","r")
fhand.readline().rstrip()
word_list = []

for line in fhand:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)
            
shorted_words = sorted(word_list)
print(shorted_words)
fhand.close()
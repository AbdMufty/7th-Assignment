fhand = open("mbox.txt","r")
fhand.readline().rstrip()
count = 1

for line in fhand:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        name = line.split()[1]
        print(name)
        count = count + 1
    
print(f"Total {count} lines were printed")
fhand.close()
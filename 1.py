file = open("qwerty.txt", "rt")
harflar = file.read()
soni = 0
for i in harflar:
    if i.isalpha():
        soni += 1
print(soni, "ta")
file.close()
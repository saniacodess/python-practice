
word = "Donkey"
with open("file.txt") as f:
    content = f.read()

newcontent = content.replace(word,"######")

with open("file.txt","w") as f:
    f.write(newcontent)

    
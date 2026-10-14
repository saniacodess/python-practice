
f = open("poem.txt")
content = f.read()

if ("twinkle" in content):
    print("The word twinkle is present in file")

else:
    print("The word twinkle is not present in file")
f.close()
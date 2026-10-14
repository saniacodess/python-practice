'''

f = open("file.txt")
data = f.read()
print(data)
f.close()
'''

#it can be writen using with statement
with open("file.txt") as f:
    print(f.read())
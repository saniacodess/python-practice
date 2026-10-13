
with open("longfile.txt", "r") as f:
    lines = f.readlines()
    lineno = 1
    for line in lines:
        if("python" in line):
                print(f"Python is presemt in line, line no.{lineno}")
                break
        lineno += 1
       

    else:
        print("python is not present")
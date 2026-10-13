
def generateTable(n):
    Table =""
    for i in range (1,11):
        Table += f"{n} x {i} = {n*i}\n"
        with open(f"Tables/Table_{n}.txt", "w") as f:
            f.write(Table)


for i in range(2,21):
    generateTable(i)
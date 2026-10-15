
def add_student():
    student = {}
    n = int(input("How many students you want to enter: "))

    for i in range(n):
        name = input("Enter Student's Name: ")
        marks = []
        m = int(input("How many marks you want to enter: "))

        for j in range(m):
            mark = int(input("Enter Student's Marks: "))
            marks.append(mark)
            student[name] = marks

    print(student)

add_student()

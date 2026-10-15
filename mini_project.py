def show_menu():
    print("             --- Student Grade Manager ---  ")
    print("-- To select the following options enter a Number --")
    print("1. Add Student")
    print("2. View Student")
    print("3. Calculate Grade")
    print("4. Exit")
    while True :
         choice = int(input("Enter a Number : "))
         if choice == 1:
             add_student()
         elif choice ==2:
             student_view()
         elif choice ==3:
             calculate_grade()
         elif choice == 4:
             print("Thankyou for using the system")
             break
         else:
             print("Invalid choice, Try again")
    

student = {}
def add_student():
    
     n = int(input("How many students you want to enter: "))
     for i in range(n):
        name = input("Enter Student's Name : ")
        marks = []
        m = int(input("How many marks you want to enter : "))
        for j in range(m):
             mark = int(input("Enter Student's Marks: "))
             marks.append(mark)
             student[name] = marks

     print(student)


def student_view():
    if not student:
        print("No student record founded!")
    else:
        for name, marks in student.items():
            print("Name : ", name  , "Marks : ", marks)


def calculate_grade():
     
     if not student:
         print("No Student record found!")
     else:
         print("Available Students: ")
         for name in student.keys():
              print("Name : ",name)

     student_name = input("Enter Student name you want to calculate grade of: ")
    
     if student_name not in student:
         print("Invalid name")    
     else:
         marks = student[student_name]
         average = sum(marks)/len(marks)
         print("average :", average ) 
         if average >= 90:
             print("Grade is A")
         elif average >=80:
             print("Grade is B")
         elif average >= 70:
             print("Grade is C")
         elif average >= 60:
             print("Grade is D")
         else:
             print("Grade is F :(")

show_menu()   
      
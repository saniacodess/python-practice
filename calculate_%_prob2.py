marks1 = int(input("Enter your numbers out of 100 : "))
marks2 = int(input("Enter your numbers out of 100 : "))
marks3 = int(input("Enter your numbers out of 100 : "))

# calculate total percentage

total_percentage = ((marks1 + marks2 + marks3)/300)*100

if(total_percentage >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congrats! You have passed.", total_percentage)

else:
    print("Sorry! You have failed, try again later.", total_percentage)
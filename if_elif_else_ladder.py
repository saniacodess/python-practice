# if_elif_else ladder

a = int(input("Enter your age : "))

if(a>=18):
    print("Welcome! You are of right age.")

elif(a<0):
    print("Invalid! This age doesn't exist.")

elif(a==0):
    print("Invalid age!")
else:
    print("Sorry! You are underage!")

    
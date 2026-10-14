p1 = "make a lot of Money"
p2 = "subscribe this"
p3 = "click here"

message = input("Enter your comment : ")

if(p1 in message or p2 in message or p3 in message):
    print("This comment is a spam")

else:
    print("This is not a spam")
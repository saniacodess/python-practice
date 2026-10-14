#Tuple are immutable 
a = (1, 33, 667, 248,)
print(type(a))

#operations and methods in Tuple
letters = (99, "Sania", 9067, "Book", 45)
print(letters.count(99)) # counting how many time sthat term comes
print(letters.index("Book")) # checking on which index it is
print(letters[1:3]) # it is called slicing
print(letters*2) # it is called repeating
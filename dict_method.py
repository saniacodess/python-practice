marks = {
    "Harry" : 89,
    "Sania" : 95,
    "Azan"  : 78,
      0     : "Ahsan"
}
print(marks , type(marks))
#methods in dictionary
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sania" : 99 , "Ruchika" : 98})
print(marks)
print(marks.get("Sania2")) # give none
print(marks["Sania2"]) # gives error

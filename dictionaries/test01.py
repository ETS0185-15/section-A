# copy()
student = {
    "name": "aymen",
    "ID": 185,
    "section": "A"
}
copied = student.copy()

print (student)
copied ["section"] = "B"
print (copied)

# clear ()

copied.clear()
print(copied)

# fromkeys()

key = ["name","dipartment","year"]


person = dict.fromkeys (key,"")
person["name"] = input ("name = ")
person["dipartment"] =input ("dipartment = ")
person["year"] =input("year = ")
print(person)
# update
person = {
    "name": "aymen",
    "id" : "0185",
    "year" : 3

}

print (person)
person.update({"year": 4,"dipartment":"EME"})
print(person)

# values

mark = {
    "phyton" : 99,
    "applied electronics": 93,
    "signal" : 90
}
print(mark)
print(mark.values())
total = sum(mark.values())
average = total/ len(mark)
print(average)
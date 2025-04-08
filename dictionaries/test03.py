person = {
    "name" : "aman",
    "age" : 69,
    "profession" : "non",
    "gender" : "male"
}
# pop()
print(person)
age = person.pop("age")
print(person)
# to print the value of age
print(f"removed:{age}") 
      
Education_level = person.pop("Education_level","N/A")
print(Education_level)

# popitem()
last_key, last_value =person.popitem()
print(person)
print(f"Removed:{last_key}={last_value}")

# setdefault()
name = person.setdefault("name","N/A")
print (person)
status = person.setdefault("status","un updated")
print (person)

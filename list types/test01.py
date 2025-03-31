# list
list = ["apple , banana,"]
append_list = list.append (["phone"])
print(list)
append_list = list.append([23])
print(list)

# clear

element = ["apple ,banana, 32"]
element.clear()
print(element)
 
# copy

original = [12,13,14,15]
new = original.copy()
new[0] = 100
new[2] = 0
print(original)
print(new)

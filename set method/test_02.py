# intersection
A = {1,2,3,4,5,6}
B = {2,4,6,8,10}
print("the value of set A =",A)
print("the value of set B =",B)
print("the intersection =",A.intersection(B))


# intersection_update
C = {1,2,3,4,5,6}
D = {2,4,6,8,10}
print("the value of set D =",D)
print("the value of set C =",C)
updated_C = C.intersection_update(D)
print("the updated intersection C =",C)

# isdisjoint
x = {1,2}
Y = {3,4}
Z = {8,2}
print("the value of set x =",x)
print("the value of set Y =",Y)
print("the value of set Z =",Z)
print(x.isdisjoint(Y))
print(x.isdisjoint(Z))
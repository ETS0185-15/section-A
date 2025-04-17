# issubset()
A = {1,2,3,}
B = {1,2,3,4,5}
print ("the value of set A =",A)
print ("the value of set B =",B)
print(A.issubset(B))

# isuperset()
C = {1,2,3,4,5,6}
D = {1,2,3,4,5}
print ("the value of set C =",C)
print ("the value of set D =",D)
print(C.issuperset(D))

#symmetric_diffrence

E ={10,15,20,25,30}
F ={0,10,20,30,40}
print ("the value of set E =",E)
print ("the value of set F =",F)
symmetric_diffrence = E.symmetric_difference(F)
print("the symmetric diffrence between setE and setF =",symmetric_diffrence)


# diffrence
setA = {1,2,3,4}
setB = {2,4,6,8}
setC = {1,7,8,9,0}
diffrence = setA.difference(setB)
diffrence2 = setA.difference(setB,setC)
print("setA =",setA)
print("setB =",setB)
print("setC =",setC)
print("diffrence of A from B =",diffrence)
print("diffrence of A from B and C =",diffrence2)

# diffrence_update
setA.difference_update(setB)
#new value for setA
print("the updatd setA=",setA)

# discard()
D = {1,2,3,4,5,5,6,7}
print("the first value of set D = ",D)
D.discard(5)
print ("the removed value (5) of setD = ",D)
D.discard(0)
print ("the removed value (0)of setD = ",D)


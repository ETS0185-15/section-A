# second update working on list method
the key differnce between string method and list method is that you can modify after creation on list method but not on string method
# test 01 
 - append()
 add any element in a list
 - clear
 remove all element in a list
 - copy 
 creates a copy of the list without removing original list
# test 02
 - count []
 count how many times a certain value appeared in the list
  list.count()
 - extend []
 add an element in the list but, unlike append it unpacks the newly added elements
 list.extend()
 - index[]
 returns the first index of a specified value in the list
# test 03
 - insert []
 add any element in the list at specific place
 list.insert(index,element)
 - pop []
 removes and returns an item at a given index
 list.pop(index)  
 list.pop() the last item
 list.pop(0) first item
 -remove []
 removes the first occerance of a specified value (not index)
 list.remove(value)
 # test 04
 -reverse[]
 reverse the order of the list
 list.revers
 -sort
 used to sort the list
 list.sort(key=none,reverse=false)
 when key = len it sort with string length
 when reverse is true it sorts with reverse
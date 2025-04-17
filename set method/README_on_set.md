# set method
# test_01
# difference()
- returns a new set containing the elements in first set but not on second.
-keeps the original set.
syntax - set.diffference(set1,set2,..)
# difference_update()
- modifies the original set by removing the elemnents found in the other set.
syntax:  set.diffference_update(set1,set2,..)
# discard()
-removes a specific element from a set if it exists (no error if missing)
syntax: set.discard(element)
# test 02
# intersection()
- returns a new set containing common elemnts between sets.
syntax : set.intersection(seta,setb,..)
# intersection_update
- modifies the original set only keeping the common elements.
syntax : set.intersection_update(seta,setb,...)
# issdisjooint()
-checks if two sets have no common elements (retuns true if disjoint)
syntax : set1.isdisjoint(set2)
# test03
# issubset()
-checks if all elements of a set are present in another set
syntax: seta.isdubset(setb)
it returns  a boolean value true or false.
# isuperset()
-checks if a set contains all elents of other set.
 syntax: seta.isuperset(setb)
it returns  a boolean value true or false.
# symmetric_differnce()
- returns elements that are in either set, but not in both.
syntax: set1.symmetric_differnce(set2)

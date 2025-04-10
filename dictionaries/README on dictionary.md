# dictionaries
Dictionaries (dict) are phython's built in key value pair data structure, optimized for fast look up.
The values are orderd changeable and fo not allow duplication.
# test01
- clear()
removes all the elements from the dictionary
- copy()
returns a copy of the dictionary
-fromkey ()
returns a specified key and value
# test02
- items()
returns a view of all key value pairs as tuples
syntax  items = dict.items()
- keys()
returns a view of all keys in the dictionary
syntax key = dict.keys()
-get()
safely retrive a value for a key (avoids keyerrors)
syntax  get = dict.get()
# test03
- pop()
removes and returns the value of specified key
safe usage of default (avoids keyerrors)
syntax value = dict.pop(key,default)
- popitem()
removes and returns the last inserted key-value pair 
syntax  key, value = dict.popitem()
- setdefault()
returns the value for key if it exists, otherwise inserts the key with default value
syntax  value = dict.setdefault(key, default)
# test04
-update()
add a value or update a value in a dictionary
syntax  dict.update(iterable_or_dict)
-values()
returns a view of all values in the dictionary
syntax values= dict.values()

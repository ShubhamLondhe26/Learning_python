#methods

#clear method
dict2={1:"String",2:"Boolean",3:"django"}
#dict2.clear()
#print(dict2)

#get method
#get_method=dict2.get(1)#will get value for specified key
#print(get_method)

#key method
#key_method=dict2.keys()#will return the key in the form of list
#print(key_method)

#value method 
#value_method=dict2.values()#will return vlues in the form of list
#print(value_method)

#item Method
#item_method=dict2.items()#wil return key:values pair in the form of tuple
#print(item_method)

#pop_method
#pop_method=dict2.pop(1)
#print(pop_method)#will remove value of spcifid key
#print(dict2)

#pop item
pop_item=dict2.popitem()
print(pop_item)#will remove last key value pair
print(dict2)



# filter -> filters items out of a sequence and returns a filtered list

def fltr(lst):
    lst2=[x for x in lst if x>2]
    return lst2

print(fltr(n))

# or

print(list(filter(lambda x:x>2,n)))



print([x for x in n if x>2])

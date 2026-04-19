#a =(1,2,3,4,5)
a = (1,32,False,"Jerry","Mohit",32)
#print(type(a))
#a[0] = 2 # In tuple we are not change the element 
print(a)

no = a.count(32)
print(no)

i = a.index("Jerry")
print(i)

repeated = a*2
print(repeated)
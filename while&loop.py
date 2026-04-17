count = 1
while count <= 5:
   # print("hello")
    count += 1

#print(count)

i = 100
while i>=1: #stopping cond
    #print(i)
    i -= 1 
#n = int(input("enter num : "))
i = 1
while i<=10:
  #  print(n*i)
    i += 1

num = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(num):
    #print(num[idx])
    idx += 1

num = (1,4,9,16,25,36,49,64,81,100)

#x = 100
#i = 0
#while i < len(num):
    #if(num[i] == x):
    # print("found at idx",i)

    #else:
     #   print("Not find")
    #i += 1

i = 1
while i <= 5:
   # print(i)
    if(i == 3):
        break
    i += 1

i = 0
while i <= 5:
    if(i == 3):
        i +=1
        continue
   # print(i)
    i += 1

#for i in range(2,10,2):
    # print(i)

#for i in range (100,0,-1):
   # print(i)

n = 3
fact = 1
i = 1
while i <= n:
    fact *=i
    i += 1
print("fact=",fact)
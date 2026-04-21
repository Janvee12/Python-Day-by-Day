#name = input("enter you name: ")
#print(name.count("$"))
#marks = int(input("enter by user: "))

#if(marks >= 90):
   #grade = "A"
#elif(marks >= 80):
    #grade = "B"
#elif(marks >=70):
 #   grade = "C"
#else:
 #   grade = "D"


#print("grade of the student ->", grade) 


#num = int(input("Enter number: "))

#rem = num % 2

#f(rem == 0):
 #   print("Even")
#lse:
 #   print("ODD")

a = int(input("enter first num: "))
b = int(input("enter first num: "))
c = int(input("enter first num: "))
d = int(input("enter first num: "))

if(a >=b and a >=c and a >=d):
    print("First is large",a)
elif(b >=c and b >=d):
    print("Second num is largest",b)
elif(c >=d):
    print("Third is largest",c)
else:
    print("Fourth num is largest",d)
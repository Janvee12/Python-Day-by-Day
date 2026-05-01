#function definition
def cal_sum(a,b): # parameters
    sum = a+b
    print(sum)
    return sum

cal_sum(3,7)#function call; arguments

cal_sum(9,23)

cal_sum(8,43)

#average of 3 no.

def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

cal_avg(2,4,3)

cities = ["delhi","Mumbai","Goa","noida"]
heroes = ["thor","ironman","captain","shaktiman"]

print(cities[0], end=" ")
print(cities[3])

def print_len(list):
    print(len(list))

print_len(cities)

n = 5

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")

converter(1)



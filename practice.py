def calc_sum(a,b):
    return a+b
sum = calc_sum(5344,6452)
print(sum)

def calc_prod(a,b=2):
    print(a*b)
    return a*b
calc_prod(9)

# print the length of the list (list is a parameter)
cities = ["delhi","mumbai","pune","kolkatta"]
heroes = ["thor","saktiman","ironman"]
def print_len(cities):
    print(len(list))

print(len(cities))
print(len(heroes))

# print the element of a list in a single line.(line is parameter)
cities = ["delhi","mumbai","pune","kolkatta"]
heroes = ["thor","saktiman","ironman"]
def print_len(list):
    print(len(list))
def print_list(list):
    for item in list:
        print(item,end = " ")

print_list(cities)
print()

# find the factorial of n.(n is parameter)
n = 5
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(4)

#  convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 43
    print(usd_val,"USD =", inr_val,"INR")
converter(87)

# Recursion
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")
show(4) # 5,4,3,2,1

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(5))

# write a recurnsion function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n==0):
        return 0
    return   calc_sum(n-1)+n
sum = calc_sum(10)
print(sum)

# write a e=recursion function to print all element in a list.
# hint: use list & index as parameter
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits = ["mango","litchi","guvava","banana"]
print_list(fruits)



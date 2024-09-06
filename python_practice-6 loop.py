count = 1
while count <=5:
    print("hello")
    count += 1
print(count)

count = 1
while count <= 2:
    print("helloworld")
    count += 1
print(count)

count = 1
while count <=100:
    print(count)
    count += 1

count = 100
while count >=1:
    print(count)
    count -= 1

count = 1
while count <=1:
    print(4*count)
    count += 1

nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["Saharukh","Salman"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1


nums = [1,4,9,16,25,36,49,64,81,100]
x = 100
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("FOUND at idx",i)
    i += 1

nums = [1,4,9,16,25,36,49,64,81,100]
x = 81
i = 0
while i < len(nums):
    if (nums[i] == x):
        print("FOUND at i", i)
    else: 
        print("finding...")
    i += 1

i = 1
while i <=6:
    print(i)
    if (i == 4):
        break
    i += 1

i = 0
while i <=5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i <= 5:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1 

vaggies  = ["garlic","onion","tomato","potato"]
for val in vaggies:
    print(val)


heroes = ["saharukh","salman","nikhil","neha"]
for val in heroes:
    print(val)

tup = (1,2,3,4,5,5)
for num in tup:
    print(num)

str = "apnacollege"
for char in str:
    if (char == 'o'):
        print("o found")
        break
    print(char)

nums = [1,4,9,16,25,36,49,64,81,100]
x = 16

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
        break
    idx += 1

seq = range(10)
for i in seq:
    print(i)

for i in range(2, 100,3):
    print(i)

for i in range(1,100):
    print(i)

for i in range(100,0,-1):
    print(i)

for i in range(1, 10):
    print(3*i)

for i in range(4):
    pass

print("give a chance ")

# find the sum  of the first n number

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =", sum)

# find the factorial of the first number

n = 4
fact = 1
i = 1
while i <=n:
    fact *= i
    i += 1
print("factorial =", fact)


marks = int(input("enter student mark : "))

if(marks >= 90):
    Grade =  "A"
elif(marks >= 80 and marks < 90):
    Grade =  "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print("grade of the student -->",Grade)

# Nesting

age = 34
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# WAP to check if a number entered by the user odd or even
num = int(input("enter num :"))

if(num % 2):
    print("odd")
else:
    print("even")

# WAP to greatest of 3 number entered by user 
a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))

if(a >= b and a >= c ):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest", c)

a = int(input("enter first number :"))
b = int(input("enter second number :"))
c = int(input("enter third number :"))
d = int(input("enter forth number :"))
if(a >= b and a >= c ):
    print("first number is largest", a)
elif(b >= c and b>=d):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest :" )
else:
    print("forth is largest", d)


# WAP to check if a number is mutiple of 7 or not
x = int(input("enter number :"))
if (x % 5 == 0):
    print("multiple of 5")
else:
    print("not a multiple")

student = ["Kanchan", 54.3,"Delhi"]
print(student) 
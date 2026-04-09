# print("helloworld")
# print("hello world")
# print("hello" + " rayan")


# age = 20
# cgpa=8.5
# iligible = True
# greeting = "hello"
# name = "rayan"
# print(greeting + ", " + name + "!" + " Your age is " + str(age) + " and your CGPA is " + str(cgpa) + ".")

# print(type(greeting))
# print(type(name))
# print(type(age))
# print(type(cgpa))
# print(type(iligible))

# # typecasting
# age_str = str(age)
# cgpa_str = str(cgpa)
# eligibility_str = str(iligible)
# print("Your age is " + age_str + " and your CGPA is " + cgpa_str + ". Eligibility: " + eligibility_str)


# # input
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello, " + name + "! Your age is " + age + ".")

# a = input("enter 1st number:")
# b = input("enter 2st number:")
# print(a+b)

# print("hello \\ world \"rayan\" \t helo ", sep="***", end="!!!")

# operators
# arithmetic operators
# a = 10
# b = 5
# print("a + b=", a + b )
# print("a - b=", a - b )
# print("a * b=", a * b )  
# print("a / b=", a / b )
# print("a % b=", a % b )
# print("a // b=", a // b )

# print ("hello, world! welcome to python ")
# print ("twinkle twinkle little star, \n how i wonder what you are, \n up above the world so high, \n like a diamond in the sky")

# a = "rayyan"
# b=21
# height = 5.8
# student =True
# print("name: " + a, "age: " + str(b), "height: " + str(height), "student: " + str(student))

# number = 24
# print(str(number +10))
# print(type(number))

# num1 = int(input("enter the number:"))
# print("the square of the number is:", num1**2)

# conditional statmenets !!!

# num1 = int(input("enter the first number:"))
# if(num1 & 1):
#     print("the number is odd")
# elif(num1 == -1):
#     print("the number is negative")    
# else:
#     print("the number is even")    

# match case statements!!!

# guess = int(input("guess the number between 1 and 5:"))
# match guess:
#     case 1:
#         print("you guessed 1 guess again")
#     case 2:
#         print("you guessed 2 guess again")
#     case 3:
#         print("you guessed 3 and you are correct")
#     case 4:
#         print("you guessed 4 guess again")
#     case 5:
#         print("you guessed 5 guess again")
#     case _:
#         print("invalid guess")

# loops

# for i in range(1,11):
#     print(i)

# num = int(input("enter the number:"))
# for i in range(1,11):
#     print(str(num), "x", str(i), "=", str(num*i) )

# while loop!!

# i=1
# while i<=10:
#     print(i)
#     i+=1

# num = int(input("enter the number:"))
# i=1
# while i<=10:
#     print(str(num), "x", str(i), "=", str(num*i) )
#     i+=1
#     if i==5:
#         break

# practice ----------

# i = int(input("enter the number:"))
# if(i>0):
#     print("posstive number")
# elif(i<0):
#     print("the number is negative")
# else:    print("the number is zero")    


# age = int(input("enter your age:"))
# if(age<18):
#     print("you are not eligible for vote")
# elif(age==18):
#     print("you can apply for vote but you are not eligible to vote")
# else:    print("you are eligible for vote")  


# num = int(input("enter the number:"))
# if(num%2==0):
#     print("the number is even")
# else:    print("the number is odd")    

# guess = int(input("guess the number between 1 and 7:"))
# match guess:
#     case 1:
#         print("its Monday")
#     case 2:
#         print("its Tuesday")
#     case 3:
#         print("its Wednesday")
#     case 4:
#         print("its Thursday")
#     case 5:
#         print("its Friday")
#     case 6:
#         print("its Saturday")
#     case 7:
#         print("its Sunday")
#     case _:
#         print("invalid guess")

# num1 = int(input("enter the number 1:"))
# num2 = int(input("enter the number 2:"))
# operation = input("enter the operation (+, -, *, /):")
# match operation:
#     case "+":
#         print("the sum is:", num1+num2)
#     case "-":
#         print("the difference is:", num1-num2)
#     case "*":
#         print("the product is:", num1*num2)
#     case "/":
#         if(num2!=0):
#             print("the quotient is:", num1/num2)
#         else:
#             print("division by zero is not allowed")
#     case _:
#         print("invalid operation")




# for i in range(1,11):
#     print(i)

# num = int(input("enter the number:"))
# for i in range(1,11):
#     print (str(num), "x", str(i), "=", str(num*i)   )

# num = 0
# for i in range(1,101):
#     num += i
# print(num)

"""
*
**
***
****
"""

# for i in range(1, 5):
#     print("$" * i)

# i = 1
# while i <=10:
#     print(i)
#     i+=1

# password= input("enter the password:")
# while password != "python123":
#     print("incorrect password, try again")
#     password = input("enter the password:")
#     print("password accepted, welcome!")

# for i in range (1,10):
#     if i ==7:
#         break
#     print(i)

# for i in range (1,10):
#     if i==5:
#         continue
#     print(i)

# for i in range(1,5):
#     match i:
#         case 1:
#             print("one")
#         case 2:
#             print("two")
#         case 3:
#             pass 
#         case 4:
#             print("four")
#         case _:
#             print("invalid number")           





# strings!!!!

# formating--------------------------------------------------------- 

# greeting="hello {} how was your day "
# name = input("enter your name:")
# # print(greeting.format(name))
# print(f"hello {name} how was your day")

# practice strings methods-------------------------------------------------

# name = " rayyanuddin sheikh  "
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())
# print(name.find("uddin"))
# print(name.replace("rayyanuddin", "rayyan"))
# print(name.split())
# print(name.join(["rayyan", "sheikh"]))
# print(name.isalpha())
# print(name.isdigit())
# print(name.startswith("  rayyan"))
# print(name.isalnum())
# print(name.count("a"))
# print(name.isspace())


# print(name)

# a = "hello"
# b = "world"
# print(f"{a} {b} ")

# text ="python programming "
# # print(text[0:6])
# print(text[-6:-1])

# TEXT = " I LOVE PYTHON PROGRAMMING "
# print(TEXT.title())
# print(TEXT.count("O"))
# print(TEXT.strip())

# TEXT1= " I LOVE PYTHON PROGRAMMING "
# TEXT=TEXT1.strip().lower()
# if (TEXT.find("a") != -1):
#     print("the letter 'a' is present in the text")
# if (TEXT.find("e") != -1):
#     print("the letter 'e' is present in the text")
# if (TEXT.find("") != -1):
#     print("the letter 'i' is present in the text")
# if (TEXT.find("o") != -1):
#     print("the letter 'o' is present in the text")
# if (TEXT.find("u") != -1):
#     print("the letter 'u' is present in the text")
# else:   
#     print("no vowel is present in the text")


# a="madama"
# b=a[::-1]
# if a==b:
#     print("the string is a palindrome")
# else:    print("the string is not a palindrome")


# functions---------------------------------------------------------

# def greet(name):
#     print(f"hello {name} how are you?")

# greet("Alice")
# greet("Bob")
# greet("Charlie")
# greet("David")

# function in javascript -----
"""
function greet(name){
console.log(`hello ${name} how are you?`);
};
"""

# lembda functions---------------------------------------------------------
# n = int(input("enter the number:"))
# square = lambda n: n**2
# print(square(n))


# practice functions---------------------------------------------------------

# def greet(name):
#     return f"hello {name} how are you?"
# name = input("enter your name:")
# print(greet(name))


# def square(n):
#     return n**2
# print(square(5))
# print(square(10))
# print(square(43))

# def area_rectangle(len,wid=10):
#     return len * wid
# print(area_rectangle(5))
# print(area_rectangle(5, 20))

# lambda function-----
# add = lambda x,y: x + y
# print(add(5, 10))
# print(add(20, 30))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))
# print(factorial(0))
# print(factorial(120))    


# def sum_of_digits(n):
#     if n==0:
#         return 0
#     else:
#           return n%10 + sum_of_digits(n//10)
# print(sum_of_digits(12345))
# print(sum_of_digits(555524))


# modules and pip---------------------------------------------------------

# import math
# print(math.sqrt(144 ))
# print(math.sin(math.radians(90)))


# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.json())


# variable scope---------------------------------------------------------

# def increment():
#     count = 0
#     count +=1
#     print(count)

# increment()
# increment()
# increment()

# def safe_devidi(a,b):
#     if b==0:
#         print("division by zero is not allowed")
#     else:
#         return a/b
    
# print(safe_devidi(10, 2))
# print(safe_devidi(10, 0))    


# list---------------------------------------------  

# marks = [85, 90, 78, 92, 88]
# print(marks)
# print(marks[0])
# print(marks[1:4])

# marks.append(95)
# marks.insert(2, 80)
# marks.remove(78)
# marks.sort()
# marks.reverse()
# marks.pop()
# marks.clear()
# marks.index(90)
# marks.count(88)
# print(marks)


# list comprehension---------------------------------------------------------


# n = int(input("enter the number:"))
# table =[i*n for i in range(1,11)]
# print(table)



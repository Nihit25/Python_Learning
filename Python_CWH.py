# print("Hello World!",7)
# print(17*13)

# This is a single-line comment 
'''In if-else statement,
It will execute block of code, if a specified condition is true
If the condition is false then it will execute another block of code
'''

# print("This will \"execute\"")
# print("Hey","Hello",sep="*",end="->")
# print("Hello World!")

# Lists are mutable and can be modified after creation
# Tuples are immutable and cannot be modified after creation

# list1=[8,2.3,[-4,5],["Apple","Banana"]]
# print(list1)
# tuple1=(("Parrot","Sparrow"),("Lion","Tiger"))
# print(tuple1)
# dict1={"name":"Sakshi","canVote":True,"age":20}
# print(dict1)
# a= complex(1,2)
# b=True
# c="Harry"
# print("The class of a is ",type(a))
# print("The class of b is ",type(b))
# print("The class of c is ",type(c))

# print("The value of 5**3 is ",5**3)
# print("The value of 20//6 is ",20//6)

# Typecasting in Python 
# a="1"
# b="2"
# print("The value of a+b without typecasting is ",a+b)
# print("The value of a+b with typecasting is ",int(a)+int(b))

# Input Functions in Python
# a=input("Enter your name: ")
# print(a)
# a=input("Enter first number: ")
# b=input("Enter second number: ")
# print(a+b)
# print(int(a)+int(b))

# friend="Apple"
# name="Harry"
# for char in name:
#     print(char)

# Slicing methods in strings
# fruit='Mango'
# len1=len(fruit)
# print("The length of the fruit Mango is ",len1)
# print(fruit[0:5])
# print(fruit[:5])
# print(fruit[-5:5])

# a="Harry!! !!!!! Harry!!"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Harry","John"))
# print(a.split(" "))
# blogHeading="introduction to jS"
# print(blogHeading.capitalize())
# str1="Welcome to the console!!!"
# print(str1.center(50))
# print(len(str1.center(50)))
# print(str1.endswith("!!!"))
# print(str1.endswith("to",4,10))
# str2="Python is an Interpreted Language"
# print(str2.startswith("Python"))
# print(str2.swapcase())
# print(str2.title())

# ApplePrice=80
# mvrn=100
# if mvrn>=ApplePrice:
#     print("Alexa, add 1 kg apples to the cart")
# else:
#     print("Alexa, do not add apples to the cart")

# num=int(input("Enter the value of number: "))
# if(num<0):
#     print("The entered number is negative")
# elif num==0:
#     print("The entered number is zero")
# else:
#     print("The entered number is positive")


# Match-case statements in Python 
# x=int(input("Enter a number: "))
# match x:
#     case 0 if x==0:
#         print("The number is zero")
#     case 4:
#         print("This is case 4")
#     case _ if x<0:
#         print("The entered number is negative")
#     case _:
#         print("None of the above cases is matched")

# name="Abhishek"
# for i in name:
#     print(i,end=", ")
# colors=["Red","Green","Blue","Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
# for k in range(1,21):
#     print(k)
# for k in range(1,12,3):
#     print(k)    

# count=5
# while (count>0):
#     print("The value of count is ",count)
#     count= count-1
# else:
#     print("This is else block")
# while True:
#     num= int(input("Enter a number "))
#     print(num)
#     if not num>0:
#         break

# for i in range(1,20):
#     print(i,end=" ")
#     if(i==6):
#         break
#     else:
#         print("Mississipi")
# print("Thank you!")
# for i in range(5):
#     if i==3:
#         continue
#     print(i)

# def name(fname,lname):
#     print("Hello!",fname,lname)
# name("Sam","Wilson")

# def name(*name):
#     print("Hello!",name[0],name[1],name[2])
# name("James","Buchanan","Barnes")

# def Name(**Name):
#     print("Hello!",Name["fname"],Name["mname"],Name["lname"])
# Name(mname="Buchanan",lname="Barnes",fname="James")

# def name(fname,mname,lname):
#     return "Hello! "+fname+" "+mname+" "+lname
# print(name("James","Buchanan","Barnes"))

# colors=["Red","Green","Blue","Yellow"]
# if "Yellow" in colors:
#     print("Yellow is present")
# else:
#     print("Yellow is absent")
    
# names=["Milo","Sarah","Bruno","Anastasia","Rosa"]    
# namesWith_O=[item for item in names if "o" in item] 
# print(namesWith_O)
# names_len=[item for item in names if len(item)>4]
# print(names_len)
# print(type(names))
# if "Ha" in "Harry":
#     print("Yes")
# lst=[i*i for i in range(10) if i%2!=0]
# print(lst)

# List methods in Python

# The reverse method reverses the order of the list 
# colors=["violet","indigo","blue","green"]
# colors.reverse()
# print(colors)
# print(colors.index("green"))
# print(colors.count("green"))
# newlst=colors.copy()
# print(newlst)
# colors.append("green")
# colors.insert(1,"orange")
# print(colors)
# print(colors+newlst)
# colors.extend(newlst)
# print(colors)
# lst.sort(reverse=True) #This sorts list in descending order
# m=l
# if m[0]=0 then changes reflect in both m and l

# countries=("Spain","Italy","India","England","Germany")
# if "Germany" in countries:
#     print("Germany is present")
# else:
#     print("Germany is absent")

# tup=(2)  #This is not a tuple
# tup=(2,)  #This is a tuple
# # tuples are immutable

#Exercise-2 Solution
# import time
# t=time.strftime("%H:%M:%S")
# print(time.strftime("%H:%M:%S"))
# hour=int(time.strftime("%H"))
# # hour=int(input("Enter hour: "))
# if(hour>=0 and hour<12):
#     print("Good Morning!")
# elif(hour>=12 and hour<16):
#     print("Good Afternoon!")
# elif(hour>=16 and hour<20):
#     print("Good Evening!")
# elif(hour>=20 and hour<24):
#     print("Good Night!")

# letter="Hey my name is {} and I am from {}"
# name="Harry"
# country="India"
# print(f"My name is {name} and I am from {country}")
# print(letter.format(name,country))
# price=49.0999
# txt=f"For only {price:.2f} dollars!"
# print(txt)

# Docstrings in python
# Python docstrings are the string literals that appear right after the  definition of a functionm, method, class or module 
# def square(n):
#     '''Takes in a number n, returns the square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(7))

# Sets in Python 
# s={2,4,2,6}
# print(s)
# info={"Carla",19,True,5.9,19}
# print(info)
# harry={}   #This is a dictionary
# harry=set()   #This is a empty set
# print(type(harry))
# for value in info:
#     print(value)

# Set methods in Python 
# cities1={"Tokyo","Madrid","Berlin","Delhi"}
# cities2={"Tokyo","Seoul","Sydney","Madrid"}
# cities3=cities1.union(cities2)
# print(cities3)
# # cities1.update(cities2)
# # print(cities1)
# # cities1.intersection_update(cities2)
# # print(cities1)
# print(cities1.difference(cities2))

# Dictionaries in Python 
# info={"name":'Karan','age':19,'eligible':True}
# print(info)
# # We can print all the keys in dictionary using keys() method 
# print(info.keys())
# # We can print all the values in dictionary using values() method 
# print(info.values())
# for key in info.keys():
#     print(f"The value corresponding to the {key} is {info[key]}")
# # We can print all the key-value pairs in dictionary using items() method 
# print(info.items())
# for key,value in info.items():
#     print(f"The value corresponding to the key {key} is {value}")
# print(info['name'])   # Karan
# print(info.get('name'))   # Karan

# Dictionary Methods in Python 
# ep1={122:45,123:89,567:69,670:69}
# ep2={222:67,566:90}
# ep1.update(ep2)
# # ep1.clear()
# # The pop() method removes the key-value pair whose key is passed as a parameter 
# ep1.pop(122)
# # The popitem() method removes the last key-value pair from the dictionary 
# ep1.popitem()
# del ep1[123]
# print(ep1)

# The else block in Python   
# for x in range(5):
#     print("Iteration number {} in for loop".format(x+1))
# else:
#     print("Else block in loop")
# print("Out of loop")

# for i in range(5):
#     print(i)
#     if i==4:
#         break
# else:
#     print("Sorry, no i")


# Exception handling in Python 
# try:
#     num=int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer")

# a=input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range (1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid Input")
# print("Some important lines of code")
# print("End of program")

# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("There is Index Error")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")

# Finally Block in Python 
# try:
#     num=int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer")
# else:
#     print("Integer accepted")
# finally:
#     print("This block is always executed")

# def funct1():
#     try:
#         l=[1,5,6,7]
#         i=int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0
#     finally:
#         print("This is always executed")
# x=funct1()
# print(x)

# Raising Custom Errors in Python       
# a=int(input("Enter any value between 5 and 9: "))
# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")


# KBC Exercise     
# questions=[
#     ["Which language was used to create FaceBook?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Instagram?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create FB?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Insta?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Webex?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Oracle?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Apple?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Edge?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Bing?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Web?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create Robot?","Python","French","JavaScript","Php","None",4],
#     ["Which language was used to create FaceBook?","Python","French","JavaScript","Php","None",4],
# ]
# levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
# money=0
# for i in range(len(questions)):
#     question=questions[i]
#     print(f"\n Question for Rs. {levels[i]}")
#     print(f"a. {question[1]}      b. {question[2]}")
#     print(f"c. {question[3]}      d. {question[4]}")
#     reply=int(input("Enter your answer (1,4) or 0 to quit:\n"))
#     if (reply==0):
#         money=levels[i-1]
#         break
#     if(reply==question[-1]):
#         print(f"It's correct answer, you have won Rs. {levels[i]}")
#         if (i==4):
#             money=10000
#         elif(i==9):
#             money=320000
#         elif(i==14):
#             money=10000000
#     else:
#         print("Sorry, it's wrong answer")
#         break
# print(f"Your take home money is {money}")


# Short hand if-else statements 
# a=33030
# b=3303
# print("A") if a>b else print("=") if a==b else print("B")
# c=9 if a>b else 0
# print(c)

# Enumerate functions in Python    
# marks=[12,56,32,98,12,45,1,4]
# # for index,mark in enumerate(marks):
# for index,mark in enumerate(marks,start=1):
#     print(index,mark)
#     if(index==3):
#         print("Harry, Awesome")

# fruits=["Apple","Banana","Mango"]
# for index, fruit in enumerate(fruits):
#     print(f"{index+1}: {fruit}")
# colors=("red","green","blue")
# for index,value in enumerate(colors):
#     print(index,value)
# s='hello'
# for index,c in enumerate(s):
#     print(index,c)

# Virtual Environment in Python 
# import pandas as pd
# print(pd.__version__)


# Import in Python 
# import math
# from math import sqrt,pi
# from math import pi, sqrt as s
# import math as math_builtin_python
# result=math_builtin_python.sqrt(p)*math_builtin_python.pi
# result=math.sqrt(9)   *math.pi
# print(result)
# print(math.nan, type(math.nan))
# print(dir(math))


    # if __name__=="__main__" in Python 
# def welcome():
#     print("Hey, you are welcome")
# if __name__=="__main__":
#     welcome()


# Encoding and decoding exercise 
# st=input("Enter message:")
# words=st.split(" ")
# coding=input("Enter 1 for coding and 0 for decoding ")
# coding=True if(coding=="1") else False
# print(coding)
# if(coding):
#     nwords=[]
#     for word in words:
#         if(len(word)>=3):
#             r1="dsf"
#             r2="jkr"
#             stnew=r1+word[1:]+word[0]+r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
# else:
#     nwords=[]
#     for word in words:
#         if(len(word)>=3):
#             stnew=word[3:-3]
#             stnew=stnew[-1]+stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))


# Local and global variables in Python  
# x=10
# def func():
#     global x
#     x=5
#     y=5
# func()
# print(x)
# # print(y)

# File I/O in Python  
# Reading a file 
# f=open('myfile.txt','r')
# # print(f)
# text=f.read()
# print(text)
# f.close()

# Wrting a file 
# f=open('myfile.txt','a')
# f.write('Hello World!')
# f.close()
# with open('myfile.txt','a') as f:
#     f.write("Hey I am inside with")


# f = open('myfile.txt', 'r')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1*2}")
#   print(f"Marks of student {i} in English is: {m2*2}")
#   print(f"Marks of student {i} in SST is: {m3*2}")

#   print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


# Lambda functions in Python  
def double(x):
    return x*2
def appl(fx,value):
    return 6+fx(value)
double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3
print(double(5))
print(cube(5))
print(avg(3,5,10))
print(appl(lambda x:x*x,5))

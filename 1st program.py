#Day 01
print("Hello world")
print("How are you \nI am fine")
print("It was a nice day wasnt it?","what do you think was it fun?")
print("Yup.It was a great day we enjoyed and have fun")
'''My day 01 was simple not much i learned little bit things but
that was enough for the start.'''


#Day 02
print("Hello world" , "with python")
print("Hello \nhow are you?")

Name = "Umar"
Age = 16
_Height = 5.10

print("My name is :", Name)
print("My age is :", Age+2)
print("My height is:", _Height)

print(type(Name))
print(type(Age))
print(type(_Height))

number= 5
isprime = True
print(type(isprime))

num=2
isprime=None
print(type(isprime))

name = "Hashir"
age = 20
height = 6.0

print(name,age,height)


#I learned about comments and data types used in python.
''' This is a
multi-line comment.'''



#Arithmetic Operations

a=10
b=5

print(a+b)#addition
print(a-b)#subtraction
print(a*b)#multiplication
print(a/b)#division
print(a%b)#modulo
print(a**b)#asterisk(used for a power b)



#Relational/Comparison Operators

a=10
b=5

print(a>b)#Greater than
print(a<b)#Smaller than
print(a>=b)#Greater than or equal
print(a<=b)#smaller than or equal
print(a==b)#(==)it means they are equal
print(a!=b)#(!=)it means they are not equal



#Assignment Operations

a=5
a+=5 #a+=5
print(a)

a-=5 #a=a-5
print (a)

a*=5 #a=a*5
print(a)

a/=5 #a=a/5
print (a)

a=5
a %= 5 #a=a%5
print (a)

a=5
a **= 5 #a=a**5
print (a)



#Logical Operations

#1.Not (logical operatior)
'''it changes the value to opposite
i.e: if the output of the data should be 
false than it will change it to true'''

variable = False

print (not variable)#=True
#Another example

print(not 10>5) 
print(not 3>5)

#2.and
'''If there are 2 pairs of data and both
are true then the output will be true.
But if one of them will be false it will be false.
if both are false it will be also false.
it gives advantage to false'''

print(5>10 and 5>2)#one is true one is false.
print(2>1 and 3>2)#both are true

#3.or
'''It is opposite to (and).it gives 
advantage to true. in it the output will only
then be false when the both data will be false.'''

print(7>11 or 4>1)
print(2<1 or 4<2)

#Operators Precedence

#order
'''   ()   
      **
     *,/,%
      +,-
  ==,!=,>,>=,<,<=
      not
      and
      or        '''

print((5+3)*2)#() its the double bracket we calculate first the value inside it.
print(5**2+5)#power is second to be calculated.
print(5*4%3/2+5)#multiply,divide and modulo is third priority.
print(5-2+3)#add and subtract are fourth priority.
print( not 5==2)
print(4>2 or 5>6 and 5>10)

a=str(10/5)
print(a , type (a))

b=bool(5)
print(b,type(b))

c=int("123")
print(c , type(c))

d=float(2)
print(d, type(d))

ans1= int(5+10.0)#this is called type casting.
ans2= 5+10.0#this is called type conversion.
print(ans1,type (ans1))
print(ans2,type(ans2))

#how to give input and how it works?

username=input("name:")
print("Welcome", username)
print("Greetings! Thanks for visiting to my 1st program.")

#sum of 2 numbers.
a=int(input("value of a:"))
b=int(input("value of b:"))

sum = a+b
print(sum)

#Average of 2 numbers.
num1 = float(input("enter 1st number="))
num2 = float(input("enter 2nd number="))

avg = (num1+num2)/2
print("average of 2 numbers=",avg)
 

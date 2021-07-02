#Python Loops

#Perhaps the most well-known statement type is the if statement.
#The body of if is executed only if the condition/ the test expression is evaluated to True.

#if condition:
    # execute these statements
#else:
    # execute these statements

# If the number is positive, we print an appropriate message
n = 3
if n > 0:
    print(n, "is a positive number.")
print("This is always printed.")
#When the variable num is equal to 3, test expression is true and statements inside the body of if are executed. If the variable num is equal to -1, test expression is false and statements inside the body of if are skipped. The print() statement falls outside of the if block (unindented). Hence, it is executed regardless of the test expression.

#The elif is short for else if. It allows us to check for multiple expressions. If the condition for if is False, it checks the condition of the next elif block and so on. If all the conditions are False, the body of else is executed.

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#A for loop is used for iterating over a sequence
#With the for loop we can execute a set of statements, once for each item in a sequence, a dictionary, a set
print("Hello")
print("Hello")
print("Hello")

#The range() function returns a sequence of numbers, starting from 0
#ends at a specified number.
#After a punctation mark colon, we write a block of commands that we want to be repeted.
#Insted of 6 there can be a variable, previosly set to some integer number within our program.
for x in range(6):
     print("Iteration", x)
  
  
 #It is possible to let the range start at another number, or to specify a different increment
for x in range(0, 10, 3):
     print (x) 
 

for x in range(-10, -100, -30):
     print (x) 

# nested for loops in Python 
  #When you have a block of code you want to run x number of times, then a block of code within that code which you want to run y number of times
  #you use what is known as a "nested loop". 
  

#from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
         print(i, end=' ')
    print()
	
  #When we want to print an integer value, we can write %d (percentage di) between quatation marks that we send to print function as an argument. Then, for each %d, we need to put a variable or an expression to be calculated and printed insted of %d.
for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' %(x, y, x*y)) 
		
fruits = ["apple", "pineapple", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "pineapple", "cherry"]
for fruit in fruits:       
   print ('Current fruit :', fruit)
print ("End!")

for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))		

#Strings as an iterable
string = "Hello World"
for x in string:
    print(x)
	
#Lists as an iterable
collection = ['hey', 5, 'd']
for x in collection:
    print(x)	

#Loop over Lists of lists
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)


words = ['cat', 'window', 'concatenate']
for w in words:
     print(w, len(w))


#break when x is 3	
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")	
	
	
	
#The following example illustrates the combination of an else statement with a for statement that searches for prime numbers from 10 through 20.	
#Prime numbers are numbers that have only 2 factors: 1 and themselves. For example, the first 5 prime numbers are 2, 3, 5, 7, and 11.
#The remainder is the integer "left over" after dividing one integer by another to produce an integer quotient (integer division). In Python (and many other programming languages) the remainder is calculated by using operator %.
for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
		#if i is a factor of num i.e. if num is dividible by i
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the next iteration of the first FOR loop
   else:                  # else part of the loop
      print (num, 'is a prime number')	
	

#While Loop: In python, while loop is used to execute a block of statements repeatedly until a given a condition is satisfied. And when the condition becomes false, the line immediately after the loop in program is executed. 

#while expression:
    #statement(s)

count = 0
while (count < 7):   
    count = count + 1
    print("Hello")	
	
count = 0
while (count < 3):   
    count = count + 1
    print("Hello")
else:
    print("In another block of statements")	

# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


#Same as with for loops, while loops can also have an optional else block. The else part is executed if the condition in the while loop evaluates to False. The while loop can be terminated with a break statement. In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false. Here is an example to illustrate this.

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
	
#On the fourth iteration, the condition in while becomes False. Hence, the else part is executed.

	
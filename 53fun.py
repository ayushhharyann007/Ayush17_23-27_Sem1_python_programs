# def my_function(a,b):   
#     return a+b
# int=my_function(10,20)
# print(int)


# def my_function(a,b):   
#     return a-b
# int=my_function(10,20)
# print(int)


# def my_function(a,b):   
#     return a*b
# int=my_function(10,20)
# print(int)


# def my_function(a,b):   
#     return a/b
# int=my_function(10,20)
# print(int)


# def my_function(a,b):   
#     return a//b
# int=my_function(10,20)
# print(int)


# def my_function(a,b):   
#     return a**b
# int=my_function(10,20)
# print(int)



# def my_function(a,b):   
#     return a%b
# int=my_function(10,20)
# print(int)





##types of arrgument in python 
# 1.positional argument
# 2.keywordbase argument

# def function(str):
#     print(str)
# function('hello worl;d')       


# def function(name,age):
#     print(name)
#     print(age)  
# function(name='ayush',age=20)        
                         
                         
                         
# def function (str1,str2):
#     print(str1)
#     print(str2)
# function('hello riya','how are you')            



# def function(*args):
#     for i in args:
#         print(i,end=" ")
# function(3)  
# function(2,1)      
# function(4,5)
# function(6,7)



# def adding(*add):
#     sum=0
#     for i in add:
#         sum=sum+i
#     print(sum)


# x=int(input('enter the first number'))
# y=int(input('enter the scond number'))  
# adding(x,y)  




        
# def subtracting(*sub):
#     sum=0
#     for i in sub:
#         sum=sum-i
#     print(sum)


# x=int(input('enter the first number'))
# y=int(input('enter the scond number'))  
# subtracting(x,y)  



# def multiplying(*mul):
#     sum=1
#     for i in mul:
#         sum=sum*i
#     print(sum)


# x=int(input('enter the first number'))
# y=int(input('enter the scond number'))  
# multiplying(x,y)  



# def avgrage(*avg):
#     sum=1
#     for i in avg:
#         sum=sum+i
#     print(sum/2)


# x=int(input('enter the first number'))
# y=int(input('enter the scond number'))  
# avgrage(x,y)  



# def function(a):
#     print(a)
    
# function (5*3+5)    
                 



     
# def add(*args):
#     sum1=sum(args)
#     return sum1


# l=int(input("Enter the total number: "))
# my_list=[]
# for i in range(l):
#     my_list.append(int(input(f"Enter value: ")))
    
# print(my_list)
# print(add(*my_list))            





# def kbfunction(*args,**kwargs):
    
#     for i in args:
#      print(i)
    
    
#     print(kwargs)
     
    
    
# kbfunction('hello','ITM',name='ayush',age=18)    


# def function(*args):
#   for i in args:  
#     print('swagat',args,'hai','apka')
# name=str(input('your name'))
# function(name)    
          
          
          
# def stu(**kwargs):
#     for i in kwargs:
#         print(i,":",kwargs[i])
# stu(Name=input("What is your Name:"),Age=input("Your AGE:"),email=input("Enter your email address"))



# def fun():
#     name = input("Enter your name:")
#     print("Welcome",name,"to ITM\nEnter your details")
# fun()
# def details(**kwargs):
#     details={}
#     for x in kwargs:
#         y=input(f"Enter your {x}: ")
#         details[x]=y
#     return details
# info=details(name="Name", age="Age", email="Email")
# print("Student Details:")
# for x, y in info.items():
#     print(f"{x}: {y}")





# def namefun(**kwargs):
#     for key, value in kwargs.items():
#         print('Welcome', value, 'to ITM!')
#         print(key, '=', value)

# choice = input('Would you like to enter a name? ')
# count = 0

# if choice.lower() == 'yes':
#     name = input('What is your name? ')
#     namefun(name=name)
# elif choice.lower() == 'no':
#     choice = input('Would you like to enter an email? ')
#     if choice.lower() == 'yes':
#         email = input('What is your email? ')
#         namefun(mail=email)
# else:
#     number = input('What is your phone number? ')
#     namefun(number=number)
    
    
    
    
# def namefun(**kwargs):
#     for key,value in kwargs.items():
#         print('Welcome',value, 'to ITM!') 
#         print(key,'=',value)
# choice=str(input('Woould you like to enter a name?'))
# count=0
# if choice=='yes':
#     n=str(input('What is your name?'))
# elif choice=='no':
#     choice=str(input('Would you like to enter email?'))
#     if choice=='yes':
#         email=str(input('What is your email?'))
#     else:
#         pass
# else:
#     numb=int(input('What is your phone number?'))



# def namefun(**kwargs):
#     for key, value in kwargs.items():
#         # print('Welcome', value, 'to ITM!')
#         print(key, '=', value)

# choice = input('Would you like to enter a name? ')
# count = 0
# if choice.lower() == 'yes':
#     name = input('What is your name? ')
#     namefun(name=name)
# if count == 0:
#     choice = input('Would you like to enter an email? ')
#     if choice.lower() == 'yes':
#         email = input('What is your email? ')
#         namefun(mail=email)
#     elif choice.lower()=='no':
#         pass
# if count==0:
#     number = input('What is your phone number? ')
#     namefun(number=number) 


 
 #variable
# var_global=4
# def func():
#     var_global=3
#     print(var_global)
    
# func()   
# print(var_global) 


# var1=10
# def fun():
#     var1=3
#     print(var1)
#     def fun2():
#         var1=4
#         print(var1)  
#     fun2()
# fun()
# print(var1)    
    



# x=3
# y=2
# def fun_name(name,age):
#     z=x+y
#     print(z)
    
    
    
# def fun_name(name="ayush",age=18)
# fun_name("ayush",19)
# fun_name("ayush",age=18)
# fun_name(age=19,20)





# def count(a):
#     print(count)

# count ((str(input("Enter name :"))))

# # count (input[])




# str="ITM SKILL UNIVERSITY"
# def helllo(str, char):
#     return str.index(char)
# print(helllo("ITM SKILL UNIVERSITY", "S"))




# def fun(string,char):
#     print(string)
#     for i in range(len(string)):
#         if char == string[i]:
#             print(i)
#     print("count is ",string.count(char))
# a = input("Enter the string ")
# b = input("Enter a char ")
# fun(a,b)



# my_string = "Hello World!"
# index = 0
# while index < len(my_string):
#     print(my_string[index])
#     index += 1
    
    
    
# str="ITM SKILL UNIVERSITY"
# def helllo(str, char):
#      return str.index(char)
# print(helllo("ITM SKILL UNIVERSITY", "S"))






# def checkOccurence(str,ch,choice):
#     if choice==1:
#         if ch in str:
#             return str.index(ch)
#         else:
#             return -1
#     elif choice==2:
#         index = 0
#         for i in range(len(str)):
#             if str[i] == ch:
#                 index = i
#                 return index
        
#         return -1
    

# str = input("Enter string: ")
# choice = int(input("1)String\n2)Char\nEnter choice: "))

# if choice==1:
#     char = input("Enter substring to find for: ")
#     index = checkOccurence(str,char,choice)
#     if index==-1:
#         print(f"'{char}' not found in string '{str}'")
#     else:
#         print(f"'{char}' found from position {index} in '{str}'")
# elif choice==2:
#     count = 0
#     char = input("Enter character to find for: ")
#     index = checkOccurence(str,char,choice)
#     for i in range(len(str)):
#         if str[i]==char:
#             count+=1
#     if index==-1:
#         print(f"'{char}' not found in string '{str}'")
#     else:
#         print(f"'{char}' found at position {index} in '{str}', total of {count} times in string")




# To find the index of a character and no of recursion in the string
# def fun(string,char):
#     return string.find(char)
# def times(string, char):
#     return string.count(char)
# def main():
#     user=input("Enter a string:")
#     search=input("Enter the character to find:")
#     index=fun(user,search)
#     count=times(user,search)
#     if index != -1:
#         print("The character",search,"is found at index:",index)
#         print("The character",search,"appears",count,"time in the string.")
#     else:
#         print("The character",search,"isn't found in the string.")
# main()






# str='''ITM SKILLS UNIVERSITY'''                                     
# print (str.find('T'))    
# print (str.find('ITM'))      
# print (str.find('SKILLS', 1))
# print (str.find('SKILLS', 1,18))





##membership opertors
# str=input("Enter the sting: ")
# print(str)
# enter=input("The word you want to find: ")

# print(str.find(enter))



#print all letter to string one which also appear in string two with using in operators

# str1="ITM SKILL UNIVERSITY"
# str2="ITM UNIVERSITY"
# com_letter= [letter for letter in str1 if letter in str2]
# print("Common one:", ''.join(com_letter))





# hello=str(input("Enter Word :"))
# hello2=str(input("Enter Word :"))
# if hello<hello2:
#     print(hello2)
# elif hello>hello2:
#     print(hello)
# elif hello==hello2:
#     print("Both Are Equal")




# print('Hi,\"whats up?\"')

# " Welcome to the ITM , KHARGHAR "
# print(" Welcome to {},{}".format("ITM","Kharghar"))
# print(" Welcome to {1},{0}".format("ITM","Kharghar"))
# print(" Welcome to {a},{b}".format(a="ITM",b="Kharghar"))







#QUESTION
# 1.wap to count number of vowels in a given string considering both upper case and lower case.
# 2. wap that takes a sentence as input and counts number of words in it.
# 3. wap to check if two strings are anagrams of each other.
# 4. wap that converts camel case string to snake case.
# 5. wap that takes a list of strings as input and sorts them based on their length.




# 1.wap to count number of vowels in a given string considering both upper case and lower case.
# vowel = ["A","E","I","O","U"]
# a = input("Enter the word : ")
# count = 0
# for i in a:
#     if i.upper() in vowel:
#         count+=1
# print(count)


#2. wap that takes a sentence as input and counts number of words in it.
# def count(sentence):
#     words=sentence.split()
#     return len(words)
# user=input("Enter a sentence:")
# result=count(user)
# print("The number of words in the sentence is:",result)

#3. WAP to check if two strings are anagrams of each other.
# def check(s1, s2):
#     if(sorted(s1)== sorted(s2)):
#         print("The strings are anagrams.") 
#     else:
#         print("The strings aren't anagrams.")         
# s1 = input("Enter the string one")
# s2 =input("Enter the second string")
# check(s1, s2)


#4. wap that converts camel case string to snake case.
# def camel_to_snake(camel_case):
#     snake_case = ''
#     for char in camel_case:
#         if char.isupper():
#             if snake_case:
#                 snake_case += '_'
#             snake_case += char.lower()
#         else:
#             snake_case += char
#     return snake_case
# c = input("Enter a camel case string: ")
# snake = camel_to_snake(c)
# print(f"Snake case string: {snake}")


#5. wap that takes a list of strings as input and sorts them based on their length.
num=eval(input("Enter the elements you want: "))
lst=[]
for i in range (num):
    liist=input("Enter list elements: ")
    lst.append(liist)
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2
print(Sorting(lst))





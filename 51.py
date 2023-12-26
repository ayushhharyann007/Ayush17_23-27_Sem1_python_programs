#WAP declare the list and print it

# x=[10,20,30,40,50]
# print("entered list is",x)

# print('element on 2nd index',x[2])
# print('element on 2nd index',x[0])
# print('element on 2nd index',x[1])
# print('element on 2nd index',x[3])


# x=['delhi','kolkata','kharghar','navimumbai']
# print("entered list is",x)

# print('element on 2nd index',x[2])
# print('element on 2nd index',x[0])
# print('element on 2nd index',x[1])
# print('element on 2nd index',x[3])



# x=['12delhi','34kolkata','93kharghar','83navimumbai']
# print("entered list is",x)

# print('element on 2nd index',x[2])
# print('element on 2nd index',x[0])
# print('element on 2nd index',x[1])
# print('element on 2nd index',x[3])




# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# print('element on 0nd index',x[0])
# print('element on 4nd index',x[3])
# print('element on 6nd index',x[5])
# print('element on 0nd to 4th index',x[0:4])

# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.append(111)
# print(x)


# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.pop(10)
# print(x)


# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.sort(reverse=True)
# print(x)

# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.remove(8)
# print(x)



# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.insert(5,130)
# print(x)


# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.extend([15,16,17])
# print(x)




# x=[10,20,30,40,50,60,70,80,90,100]
# print(x)
# x.reverse()
# print(x)



# list1 = [11,22,33,44,55,66,77,88,99,110]
# even = []
# odd = []

# for num in list1:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print(list1)
# print(even)
# print(odd)





# x=[10,20,30,40,50]
# print(x)
# x.extend([60,70,80])
# print(x)


# x=[10,20,30,40,50]
# y=[60,70,80]
# z = x + y
# x.append(y)
# print(x)
# print(z)

# a=float(input("Enter first num:"))
# b=float(input("Enter second num:"))
# c=float(input("enter the third num:"))

# print('avg of three num is:',(a+b+c)/3) 




x=[[2,5,7],[1,3,6]]
y=[[2,5,6],[1,3,7]]
result=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j] + y[i][j]
print(result)
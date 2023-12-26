#WAP that creates a list of random integer
#to print index at which particular value exits . if value exists at multiple location in the list , 
# then print all the indices also count the number of times the value is repeated in the list

# num_list = [1,2,3,4,5,6,7,8,9,]
# num = int(input("enter the numbr"))
# i=0
# count=0
# while i<len(num_list):
#     if num==num_list[i]:
#         print(num,"found at location")
#         count+=1
#     i+=1
# print(num,"appears",count,"times in the list")        


#WAP that forms a list of first charcter in evry word in another list

# words = ['ashlin', 'riya', 'akriti', 'bhagyshree', 'sahil','prem']
# charList = []
# for word in words:
#     charList.append(word[0])

# print(charList)



x=[[2,5],[1,3]]
y=[[2,5],[1,3]]
result=[[0,0,],[0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j] + y[i][j]
print(result)


x=[[2,5,7],[1,3,6]]
y=[[2,5,6],[1,3,7]]
result=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j] + y[i][j]
print(result)
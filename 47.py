#multiDimensional list

# x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])


# subl=[['male','female'],['akriti','bhagyshree']]
# x=[[1,2.4,3,'Ayush'],[5,6,'sahil',8.7],['riya',10,1.11,12],[13,14.6,'ashlin',subl[0]]]



# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(subl)


# print(len(x))



# WAP to find smallest and larget number in the list.
n=int(input('Enter number of elements: '))
L=[]
for i in range(n):
    L.append(int(input(f"enter {i+1}st number :")))
print(L)
print(max(L))
print(min(L))


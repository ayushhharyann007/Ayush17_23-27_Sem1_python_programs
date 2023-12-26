#WAP to demonstrate diffrent method of list


x=[1,2,3,4,5,6,7,8,9]
print(x)

x.append(12)
print(x)
#L.append() adds one item to the end of the list.

x.extend([15,16,17])
print(x)
#L.extend()adds multiple item


x.pop(5)
print(x)
#l.pop()remove element from default

x.reverse()
print(x)
#l.reverse() reverse the list 

x.insert(20,17)
print(x)
#l.insert() insert the new item in the list 

x.remove(8)
print(x)
#l.remove() remove the item from the list

x.sort(reverse=False)
print(x)
#l.sort()sorting the item in ur list 
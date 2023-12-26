
#write a python program to create list tuple and dict.

d={1:'Ayush',"roll":17,"stu":[36,"Ayush.Aryan",15011]}
print(d)

print(d["stu"])

#add/modify
print("#add/modify")
d["stu"]=d["stu"].append("ITM")

print(d["stu"])
print(d)

#delete
print("#delete")
del(d['roll'])
print(d)

#dictonaries i dictonaries
p={}
d={'p':{1:'Ayush',"roll":17,"stu":[36,"Ayush Aryan"]}}
print()


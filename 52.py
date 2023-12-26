#WAP in python program to unpack a tupple in several variable 
# x = (1, 2, 3)
# a, b, c = x
# print(a)
# print(b)
# print(c)


#WAP python to remove an empty tuples from thr list of tuples

# a = [(),(),(""),('a','b'),('a','b','c'),('d')]
# print(a)

# b = [(),(),(""),('a','b'),('a','b','c'),('d')]
# b.remove(())
# b.remove(())
# b.remove((''))
# print(b)

# c= [(),(),(""),('a','b'),('a','b','c'),('d')]
# print(c)
# c=[x for x in c if x!=x]
# print(c)



#to unzip a list of tupples int individual list

# d = [(),(),(""),('a','b'),('a','b','c'),('d')]
# d = [d(x) for x in zip(*d)]
# print(d)


#wap to calculate parking charges of a vehicle.
#Enter the type of vehicle as a character (c for car , b for bus etc) and no of hrs, then calculate charges as given below 
#truck/bus-20rupees per hr , car-10rupees per hr , scooter/cycle/bile - 5rupees per bus

# type=["car","scooter","cycle","bike","truck","bus"]
# print("Ticket generator\n1)TRUCK or BUS\n2)CAR\n3)SCOOTER, CYCLE or BIKE\n")
# choice=input("Enter your respective vehicle choice:")
# h=float(input("Enter number of hours:"))
# if choice==1:
#     print("Amount to be paid is:",h*20)
# elif choice==2:
#     print("Amount to be paid is:",h*10)
# else:
#     print("Amount to be paid is:",h*5)


# WAP to calculate parking charges of a vehicle. Enter the type of vehicle as a character(c=car,b=bus,etc,.)and number of hours, then calculate charges as given below:
# scooter,cycle,bike -- RS.5
# car -- Rs.10
# truck/bus -- Rs.20
# To be modified:in and out time(24 hour scale) and generate receipt
# if parked for more than  3 hours. New charges:
# scooter,cycle,bike=Rs.10
# truck,bus=Rs.30
#  car=Rs.20

# print("PLEASE ENTER THE TYPE OF VEHICAL")
# print("'C' for car, 'B' for bus,'T' for truck,'S' for scooty")



# ch=input("Enter the type of vehical")
# timecheckin=(float(input("Enter checkin time")))
# timecheckout=(float(input("Enter checkout time")))
# timediff=(timecheckout-timecheckin)

# if ch=='C':
#     if timediff>3:
#      print(10*timediff,"RS you will have to pay")
#     elif timediff<=3:
#        print("You will have to pay RS 20")

# elif ch=='B':
#    if timediff>3:
#      print(20*timediff,"RS you will have to pay")
# elif timediff<=3:
#        print("You will have to pay RS 30") 
   

# elif ch=='T':
#     if timediff>3:
#      print(20*timediff,"RS You will have to pay")
#     elif timediff<=3:
#        print("You will have to pay RS 30")

# elif ch=='S':
#     if timediff>3:
#      print(5*timediff,"RS You will have to pay")
#     elif timediff<=3:
#        print("You will have to pay RS 10")


#WAP that creates a dic of cubes of odd numbers 


# cubes = {i: i**3 for i in range(1, 11) if i % 2 != 0}
# print(cubes)




# students=(
#     ('Ashlin', (85, 90, 92, 88, 95)),
#     ('Akriti', (78, 85, 90, 80, 88)),
#     ('Bhagyaashree', (92, 88, 85, 90, 95)),
#     ('Riya', (80, 82, 78, 85, 90)),
# )
# students = (
#     ('Alice', (85, 90, 92, 88, 95)),
#     ('Bob', (78, 85, 90, 80, 88)),
#     ('Charlie', (92, 88, 85, 90, 95)),
#     ('Diana', (80, 82, 78, 85, 90)),
#     ('Eve', (90, 92, 88, 85, 78))
# )
# topper = max(students, key=lambda student: sum(student[1]))
# topper_name = topper[0]
# topper_marks = topper[1]
# topper_info = (topper_name, topper_marks)
# print(topper_info)

#1
# x=[1,2,3,4,5]
# y=(5,4,3,2,1)
# a=x.append(y)
# print(x)


#2
# x=(66,55,88,'car',87.65)
# print(len(x))




#3
# cubes = {i: i**3 for i in range(1, 21) if i % 2 != 0}
# print(cubes)



#4
cubes={i: i**3 for i in range(1,21)}
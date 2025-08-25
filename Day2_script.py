"""

my_list=[10,20,"python",2.5]
print(my_list)
for i in my_list:
    print(i)
    print("Bye")
    print(type(i))

my_list=[10,20,"python",2.5]
print(f"Total lenght of my list is:{len(my_list)}")
print(my_list[0])
print(my_list[-1])

#replace
print(id(my_list))
my_list[0]='Java'
print (my_list)
print(id(my_list))



my_list=[10,20,"python",2.5]
new=['java','Tanisha']
for i in new:
    my_list.append(i)
print(my_list)



my_list=[10,20,"python",2.5]
my_list.extend([100,'Tanisha'])
print(my_list)



my_list=[10,20,"python",2.5]
print(id(my_list))
my_list.clear()
print(my_list)
print(id(my_list))


my_list=[10,20,"python",2.5]
print(my_list)
del (my_list)
print(my_list)

mylist=[10,20,30,10,50,10]
print(mylist)
mylist.count([10])


mylist=[10,20,30,10,50,10]
print(mylist)
mylist.sort()
print(mylist)


mylist=[10,20,30,10,50,10,100,80,90]
print(sorted(mylist))
x=sorted(mylist)
print(mylist)
print(x)


mylist=[10,20,30,50,10,100,80,90]
mylist1=mylist
print(f"id of mylist={id(mylist)}")
print(f"id of mylist1={id(mylist1)}")
mylist.append(100)
print(mylist)
print(mylist1)



mylist=[10,20,30,50,10,100,80,90]
mylist1=mylist.copy()
print(f"id of mylist={id(mylist)}")
print(f"id of mylist1={id(mylist1)}")
mylist.append(100)
print(mylist)
print(mylist1)


mylist=[10,20,30]
mylist.append([11,22,33])
print(mylist)
print(mylist[-1])
print(mylist[-1][-1])



x=(100) #int
a=(100,) #tuple
print(a)
print(type(a))
print(x)
print(type(x))
y=8,
print(y)
print(type(y))

u=('python','java')
print(u)
print(type(u))

v='python','java'
print(v)
print(type(v))


mylist=[10,20,30,(11,22,33),[100,200,300]]




emp_data={101:'Tanisha',102:'Barath',103:'Shreya'}
print(emp_data)
print(emp_data[101])
print(emp_data[102])
for i in emp_data:
    print(i,":",emp_data[i])


emp_data={101:['Tanisha','Evergent','DW'],102:'Barath',103:'Shreya'}
print(emp_data[101])
print(emp_data[101][-1])
emp_data[101][-1]='QA'
print(emp_data)



emp_data={101:'Tanisha',102:'Barath',103:'Shreya'}
for k,v in emp_data.items():
    print(k,"-->",v)


emp_data={101:'Tanisha',102:'Barath',103:'Shreya'}
print(103 in emp_data)
emp_data[103]='Ram'
print(104 in emp_data)
emp_data[104]='Shreya'
for k,v in emp_data.items():
    print(k,"-->",v)



x={10,20,30,40,10,30,90}
print(x)
print(id(x))
for i in x:
    print(i)

x.add(100)
print(x)
print(id(x))



x={10,20,30,40}
y={11,20,30}
print(x.intersection(y))
print(x)
x.intersection_update(y)
print(x)
y.intersection_update(x)
print(y)



x=int(input("Enter a num1:"))
y=int(input("Enter a num2:"))
print(f"sum of {x} and {y}={x+y}")
print(f"sub of {x} and {y}={x-y}")
print(f"mul of {x} and {y}={x*y}")
print(f"div of {x} and {y}={x/y}")
print(f"power of {x} and {y}={x**y}")
print(f"mod of {x} and {y}={x%y}")
print(f"floor of {x} and {y}={x//y}")



x=10
y=20
z=100
print(x<y) #True
print(x>y) #False
print(x>y and z<x) #False
print(x<y or z>x) #True
print(x<y and z<y) #False
print("B"*20)



x=int(input("Enter a num1:"))
if x>0:
    print(f"{x} is a positive number")
print(f"Bye")



x=int(input("Enter a num1:"))
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")

print("Bye")


x=int(input("Enter a num1:"))
if x>=100 and x<1000:
    print(f"{x} is 3digit num")
else:
    print(f"{x} is not a 3digit num")

print("Bye")


x=int(input("Enter a num1:"))
if x>0:
    print(f"{x} is a positive number")
    if x<10:
        print(f"{x} is a single digit num")
    else :
        print(f"{x} is not a single digit num")
else:
    print(f"{x} is not positive num")
print(f"Bye")



x=int(input("Enter a num1:"))
if x>0:
    print(f"{x} is a positive number")
elif x<0:
    print(f"{x} is a negative number")
else:
    print(f"Given num is 0")


import os
os.system('cls')
print("\n\n\n\n\n\t\t\t\t\tcalculator\n\t\t\t\t\t************\n1.SUM\n2.SUB\n")
op1=int(input("Enter your option:"))
if op1==1:
    x=int(input("Enter num1:"))
    y= int(input("Enter num2:"))
    print(f"sum={x+y}")
elif op1==2:
    x=int(input("Enter num1:"))
    y= int(input("Enter num2:"))
    print(f"sub={x-y}")
else:
    print("Wrong option Try again")




i=1
while i<=10:
    print(i)
    i+=1
print("bye")

i=1
while i<=10:
    print(i)
    if i==6:
        break
    i+=1
print("bye")


i=1
while i<=10:
    if i==6:
        i += 1
        continue
    print(i)
    i += 1
print("bye")


for i in range(1,11):
    if i==5:
        continue
    print(i)



f=open('test1.txt','r')
print(f)
445


f=open('test1.txt','r')
print(f)
x=f.read()
print(x)
f.close()
print(type(x))



with open('test1.txt') as FO:
    for i in FO:
        print(i,end="")
print("Bye")



with open('test1.txt') as fo:
    x=fo.readlines()
for i in x[1:]:
    print(i,end="")

"""
with open('test11.txt','w+') as fo:
    fo.write("Hi python\nBye python\n")
    # fo.seek(0)
    x=fo.readlines()

print(x)
for i in x:
    print(i,end="")

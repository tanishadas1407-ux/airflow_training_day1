# import re
# with open('test1.txt','r') as fo:
#     for i in fo:
#         if re.search('Python',i):
#             print(i,end="")

r"""
import re
with open('test1.txt','r') as fo:
    for i in fo:
        #if re.search('[6-9][0-9]{9}',i):
        if re.search(r'\w+[@]+[a-z]+[.][a-z A-z]',i):
            print(i, end="")


print("Hi")
def f1():
    print("Tanisha")
    print("python")
    print("Training")
f1()
print("bye")
f1()


#function with argument:
def cal(x,y):
    print(x+y)
    print(x-y)
    print(x/y)
cal(9,10)
cal(5.6,2)


#scope of variable
a=10
def test():
    b=20
    print('I am in Test',a)
    print('I am in Test', b)
    print('I am in Test',d)

d=100
test()

def test1():
    c=20
    print('I am in Test',a+c)
    print('I am in Test', c)

test1()



def f1(x,y):
    #print x+y
    return(x+y)
k=f1(100,200)
print(k)
print(f1(10,20))



def intro(name,company):
    print(f"my name is {name},I am working at {company}.")
intro(name='Tanisha',company='evergent')
intro('Barath','wisig')
intro(company='netenrich',name='shreya')



def f1(x,y,z=0):
    print(x)
    print(y)
    print(z)
    print('*'* 10)

f1(100,200,300)
f1(100,200)


def f1(x,y,op='+'):
    if op=='+':
        print(x+y)
    elif op=='-':
        print(x-y)

f1(100,200)
f1(200,100,'-')




def intro(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
intro(name='Tanisha',place='Hyd')

intro(name='xyz',id=123)


import arithmatic
x=int(input('Enter a num1:'))
y=int(input('Enter a num2:'))
s1=arithmatic.sum(100,10)
s2=arithmatic.sub(100,10)
print(s1)
print(s2)



import mymath

x=int(input('Enter a num1:'))
y=int(input('Enter a num2:'))
s1=mymath.sum(x,y)
s2=mymath.mul(x,y)
s3=mymath.sub(x,y)
print(f"sum={s1},sub={s3},mul={s2}")

"""

import pandas

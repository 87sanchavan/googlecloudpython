print (__name__)
print(__name__)

tup1 = (1,2,3,"HJiiii")
tup2= (4,5,6,3,4,5)
tup3= 3,5,6,67,3

import sys
print(tup1)
print(tup2)

paths = sys.path

print(tup3.count(3))
#for a in paths:
 #   print(a)



    #!/usr/bin/python

Money = 2000
def AddMoney():
    # Uncomment the following line to fix the code:
    global Money
    Money =  1000;

print (Money)
AddMoney()
print (Money)


myGlobal = 5

def func1():
  global  myGlobal
  myGlobal = 42 ;

def func2():
    print(myGlobal)

func1()
func2()


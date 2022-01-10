from math import *
from numpy import *


def digitcount():
    global d
    global norder
    for i in range(1,15):
        f1 = norder - pow(10,i)
        if f1 < 0:
            d = i
            break


def numorder():
    global d
    global norder
    x = norder
    for i in range(0,d):
        arr1[i] = x % 10
        x = (x - arr1[i]) / 10
    list1 = []
    for j in range(0,d):
        list1.append(arr1[j])
        list1.sort()
    for k in range(0,d):
        arr1[k] = list1[k]
    x = 0
    for l in range(0,d):
        x = int(x + arr1[l] * pow(10,d-l-1))
        norder = x


def reverse():
    global nreverse
    global d
    nreverse = 0
    for i in range(0,d):
        nreverse = int(nreverse + arr1[i] * pow(10,i))


def substraction():
    global norder
    global nreverse
    global sub
    sub = abs(nreverse - norder)



#program starts from here
z = 30
d , l , m , s , sub , nreverse = 0 , 0 , 0 , 0 , 0 , 0
subarray = zeros(z,longdouble)
norder = longdouble(input('enter any number to check: '))
digitcount()
arr1 = zeros(d,longdouble)
for j in range(0,z):
    digitcount()
    print('number is: ',norder)
    print('number of digits are: ',d)
    numorder()
    print('sorted number is: ',norder)
    reverse()
    print('reverse number is: ',nreverse)
    substraction()
    subarray[s] = sub
    sub = 0
    print('after substraction result: ',subarray[s])
    digitcount()
    if subarray[s] - pow(10,d-1) < 0:
        subarray[s] = subarray[s] * 10
    s = s + 1
    print('')
    if s != 1 and subarray[s-1] == subarray[s-2]:
            print('we got our kaprekar constant for the given number of digits: ',subarray[s-1])
            l = l + 1  
    if l != 0:
        print('thankyou')
        break
    if s != 1:
        for i in range(0,s-1):
            if subarray[s-1] == subarray[i]:
                m = m + 1
    if m != 0:
        print('loop generated, thankyou')
        break
    norder = subarray[s-1]
    nreverse = 0
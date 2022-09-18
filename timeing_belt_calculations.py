from cmath import sqrt
import math
from math import pow
n1 = 20 #number of teeth
n2 = 120
pd1=(n1*2)/3.14159265359 #(number of teeth x pitch of the pulley)/pi
pd2=(n2*2)/3.14159265359
belt_length=400
a=(4*belt_length)-6.28*(pd1+pd2)
b=pow(a,2)
c=pd1-pd2
pow1=pow(c,2)
sqrt1= math.sqrt(b-(32*pow1))
centre_distance=(a+sqrt1)/16
print("Center distance = " ,centre_distance)
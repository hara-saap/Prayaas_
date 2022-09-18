

######## USE THIS CODE TO CALCULATE THE CENTRE DISTANCE OF PARALLEL TIMING PULLEYS FOR GIVEN BELT LENGTH AND NUMBER OF TEETH OF THE 2 PULLEYS #########

######## USE THIS CODE TO CALCULATE THE CENTRE DISTANCE OF PARALLEL TIMING PULLEYS FOR GIVEN BELT LENGTH AND NUMBER OF TEETH OF THE 2 PULLEYS #########

######## Contact for doubts: manujaaain@gmail.com #########


from cmath import sqrt
import math
from math import pow
n1 = 20 #number of teeth
n2 = 80
pitch_of_belt = 2 ### FOR GT2 ITS 2mm
pd1=(n1*pitch_of_belt)/3.14159265359 #(number of teeth x pitch of the pulley)/pi
pd2=(n2*pitch_of_belt)/3.14159265359
belt_length=280
a=(4*belt_length)-6.28*(pd1+pd2)
b=pow(a,2)
c=pd1-pd2
pow1=pow(c,2)
sqrt1= math.sqrt(b-(32*pow1))
centre_distance=(a+sqrt1)/16
print("Center distance = " ,centre_distance)

# import numpy as np
# a=np.random.randn(1,3) 

# b = np.random.randn(3, 3)

# c = a*b
# print(c.shape)
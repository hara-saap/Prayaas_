

######### USE THIS CODE TO CALCULATE THE BELT LENGTH NEEDED FOR PARALLEL TIMING PULLEYS FOR GIVEN CENTRE DISTANCE AND NUMBER OF TEETH OF THE 2 PULLEYS #########

######### USE THIS CODE TO CALCULATE THE BELT LENGTH NEEDED FOR PARALLEL TIMING PULLEYS FOR GIVEN CENTRE DISTANCE AND NUMBER OF TEETH OF THE 2 PULLEYS #########

######### Contact for doubts: manujaaain@gmail.com #########


from cmath import sqrt
import math
from math import pow
n1 = 20
n2 = 160
pitch_of_belt = 2 ### FOR GT2 ITS 2mm
pd1=(n1*pitch_of_belt)/3.14159265359 #(number of teeth x pitch of the pulley)/pi
pd2=(n2*pitch_of_belt)/3.14159265359
cd = 102.6 #centre distance
a = 3.14159265359*(pd1+pd2)*0.5+2*(cd)
b=pd1-pd2
pow1= pow(b,2)
c=pow1/(4*cd)
belt_length = a+c
print("belt_length needed : ", belt_length)
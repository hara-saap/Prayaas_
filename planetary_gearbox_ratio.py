
######################### CHANGE THE TEETH VALUES AS PER YOUR NEEDS #########################

######### Contact for doubts: manujaaain@gmail.com #########


import math

for k in range(3,6):  #number of planets, you can change the 6 to a higher value if you want more planets.
    for i in range(12,17): #number of teeth of sun gear
        for j in range(10,70):  #number of teeth of planet gear
            nr= i+2*j  #number of teeth of ring gear
            check = (nr +i)/k
            intcheck= int(check)  #creating this to check if the value is whole number or not 
            ratio= (nr/i)+1    #final ratio
            if (check==intcheck):
                print("Number of Planets : ", k, "Planet teeth : ",j, "Sun teeth : ",i,"Ring teeth : ", nr, "Ratio : ", ratio)




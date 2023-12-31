# Wilson model of Propylene Oxide & Acetone
# Here 1 - Propylene Oxide 2 - Acetone
import math
import numpy as np
import matplotlib.pyplot as plt

# for Propylene Oxide
A1 = 7.01443
B1 = 1086.369
C1 = 228.594
V1 = 70.75

# for Acetone 
A2 = 7.11714
B2 = 1210.595
C2 = 229.664
V2 = 74.04

R = 1.987
P_t = 760 #mm Hg

# for wilson model constant
A12 = 7.0259
A21 = -11.2050

# taking x (mole fraction in liquid phase value)    
x1 = np.linspace(0.0,1.0,num=100)
x2 = 1 - x1
#print(x1)

# Calculating t_sat values where P = P_t
t1_sat = (B1/(A1-np.log10(P_t))) - C1 # using Antoine Vapor Pressure Equation
t2_sat = (B2/(A2-np.log10(P_t))) - C2

# making a 1X100 zero array for y(mole fraction in vapor phase)
y1 = np.zeros(100)
# y2 = np.zeros(100)
# print(y1)
t_sat=np.zeros(100)

for i in range(0,100):
    t_sat[i] = x1[i]*t1_sat + x2[i]*t2_sat

    # Using Antoine Vapor Pressure Equation
    P1_sat = 10**(A1-(B1/(t_sat[i]+C1))) 
    P2_sat = 10**(A2-(B2/(t_sat[i]+C2)))

    
    # Using Wilson Model
    L12 = (V2/V1)*np.exp(-A12/(R*t_sat[i]))
    L21 = (V1/V2)*np.exp(-A21/(R*t_sat[i]))
    lam_1 = -np.log(x1[i]+L12*x2[i]) + x2[i]*( L12/(x1[i]+L12*x2[i]) - L21/(x2[i]+L21*x1[i]) )
    lam_2 = -np.log(x2[i]+L21*x1[i]) - x1[i]*( L12/(x1[i]+L12*x2[i]) - L21/(x2[i]+L21*x1[i]) )
    gamma_1 = np.exp(lam_1) 
    gamma_2 = np.exp(lam_2)

    # using law of partial pressure
    P_total = x1[i]*gamma_1*P1_sat + x2[i]*gamma_2*P2_sat

    #Using Raoult's Law
    y1[i] = (x1[i]*gamma_1*P1_sat)/P_total
    # y2[i] = 1 - y1[i]

# Taking experimental Data
t_exp =  [56.20,55.20,54.10,53.00,51.90,50.80,49.40,46.10,43.40,43.00,40.00,38.20,36.70,35.90,35.10,34.10]
x1_exp = [0.00,0.0321,0.0723,0.1045,0.1416,0.1812,0.2378,0.3745,0.5058,0.5599,0.6618,0.7579,0.8435,0.8929,0.9465,1.00]
y1_exp = [0.00,0.0650,0.1410,0.2012,0.2594,0.3293,0.4007,0.5602,0.6753,0.7373,0.8129,0.8759,0.9257,0.9489,0.9761,1.00]

# Plotting T V/s x,y
plt.plot(x1,t_sat,'r')
plt.plot(y1,t_sat,'g')
plt.plot(x1_exp,t_exp,'b--')
plt.plot(y1_exp,t_exp,'c--')
plt.legend(["x1","y1","x1_sat","y1_sat"])
plt.xlabel("x1,y1")
plt.ylabel("T")
plt.show()

# Ploting y V/s x 
plt.plot(x1,y1,'b')
plt.plot(x1_exp,y1_exp,'r--')
plt.legend(["x1","x1_exp"])
plt.xlabel("x1")
plt.ylabel("y1")

plt.show()
    
# END OF THE CODE




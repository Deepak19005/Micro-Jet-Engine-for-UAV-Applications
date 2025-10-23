import math as m
import numpy as np

cp = 1001
#rc = 3   #required compresson ratio
T_in = 300  #Inlet Temperature
gamma = 1.402  #Air Gamma at inlet
beta1 = np.radians(22.22)     #Blade angle at inlet
beta2 = np.radians(30.05)       #Blade angle at exit
rho_T_in = 1.17605  #Density of air at Inlet
rho_T_0 = 1.54
N = 10000  #RPM
dim_rat = 10/22.7838  #dimention ratio between 
r1 = (2.18)*(0.0254)*(dim_rat)   #Inlet blade ratio
r2 = (4.46)*(0.0254)*(dim_rat)  #Outlet Blade ratio
rt =(2.87)*(0.0254)*(dim_rat)  #Inlet Blade Outer radius
rh =(1.49)*(0.0254)*(dim_rat)  #Inlet Max radius of the Eye Cone
rd = 0.15
t1 = (0.02)*(0.0254)*(dim_rat)    #Thickness of blade at inlet
t2 = (0.08)*(0.0254)*(dim_rat)     #Thickness of blade at exit
b1 = (1.37)*(0.0254)*(dim_rat)     #Blade dimention along axis at inlet
b2 = (0.48)*(0.0254)*(dim_rat)     #Blade dimention along axis at exit
n1 = 11   #Number of blades at inlet
n2 = 22   #Number of blades + No of flow seperators
Ain = m.pi*(pow(rt,2)-pow(rh,2))



u1 = 2*N*r1*m.pi/60 #Velocity of the Blade Tip at inlet
u2 = 2*N*r2*m.pi/60 #Velocity of the Blade Tip at outlet
n_imp = 0.7  #Assumed Efficiency of the compressor
slip_factor = 1-(0.63*m.pi)/(n1)    #Given by Stannitz formula
m_dot = (1-slip_factor)*rho_T_0*(2*m.pi*r2-n2*t1)*b2*(u2)*(m.tan(beta2))  #Mass flow rate
v_in = m_dot/(Ain*rho_T_in)
rc = pow(1+(n_imp*slip_factor*u2*(u2-(m_dot/(2*m.pi*r2*b2*m.tan(beta2))))/((T_in+(pow(v_in,2)/(2*cp)))*cp)),(gamma/(gamma-1)))  #Total Pressure Ratio
cr1 = m_dot/(rho_T_in*2*m.pi*r1*b1)  #Radial velocity component at inlet
cr2 = m_dot/(rho_T_in*2*m.pi*r2*b2)  #Radial velocity component at exit
w1 = cr1/m.sin(beta1)  #relative velocity of air at inlet
w2 = cr2/m.sin(beta2)  #relative velocity of air at exit
c1 = pow((pow(cr1,2)+pow(cr1,2)),0.5)  #
c2 = pow((pow(cr2,2)+pow(cr2,2)),0.5)
ct1 = u1 - w1*m.cos(beta1)  #Tangential velocity component at inlet
ct2 = u2 - w2*m.cos(beta2)  #Tangential velocity component at exit
n = 0.8  #Assumed efficiency
alpha1 = m.atan(cr1/ct1)
alpha2 = m.atan(cr2/ct2)
power_required = slip_factor*m_dot*pow(u2,2)/(n)  #Power required to run the compressor at N rpm including effeciency



print("RPM of Motor : "+str(N) + " rpm")
print("Power : "+ str(power_required) + " Watt")
print("Torque : "+str(power_required/(N*2*m.pi/60)) + " N-m")
print("mass flow rate : "+str(m_dot) + " Kg/s")
print("mass flow rate : "+str(m_dot*0.7) + " Kg/s")
print("Total Pressure Ratio : "+str(rc))
print("Velocity of blade tip at outlet of impeller : "+str(u2) + " m/s")
print("Velocity of blade tip at intlet of impeller : "+str(u1) + " m/s")
print("Area of exit : "+str(2*m.pi*r2*b2) + " m^2")
print("Velocity of Inlet : "+str(v_in) + " m/s")
print("Velocity of exit : "+str(m_dot/(2*m.pi*r2*b2*rho_T_0)) + " m/s")
print("Absolute air inlet angle: " + str(alpha1)+ " degrees")
print("Absolute air inlet angle: " + str(alpha2)+ " degrees")



#V_w2 = 0
#slip = (N*2*r2/2)-V_w2
#slip_factor = V_w2/(N*2*r2/2)
#m_dot1 = 2*m.pi*r2*b2*rho_T_in*(T_in+(pow(v_in,2)/(2*cp)))*(u2-(slip_factor*u2/m.tan(beta2)))
#vw2 = u2 - vr2*m.cos(beta1)
#Torque = m_dot*u2  #Torque
#power = Torque*2*m.pi*(N/(n_imp*60))  #Power
#slip_factor = 0.85 #This is the general value of slip factor in practical sinarios
#Cu1 = u1 - (m_dot/(rho_T_in*2*m.pi*r1*b1))*m.tan(beta1)  
#Cu2 = u2 - (m_dot/(rho_T_in*2*m.pi*r2*b2))*m.tan(beta2)  


#print("Power1 : "+ str(power) + " Watt")
#print("Work per unit mass: "+str(work) + " Joules")
#print("mass flow rate2 : "+str(m_dot1) + " Kg/s")
#print(str(2*m.pi*0.01*rho_T_in*pow(r2,3)*N/60))
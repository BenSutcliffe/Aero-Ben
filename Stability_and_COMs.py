import numpy as np
from matplotlib import pyplot as plt

##### FUNCTIONS TO DETERMINE COM TAKEN "GRIFFIN STRESSES WITH TIME" ON DRIVE ######

R = 0.375/2 # rocket radius in metres
T_ox = 2.3e-3 # LOX tank wall thickness in metres
T_fuel = 2.3e-3 # fuel tank wall thicknenss in metres
T_aero_top = 1e-3 # top aerocover thickness in metres
T_aero_inter = 1e-3 # bottom aerocover thickness in metres
T_aero_fin = 1e-3 # find can aerocover thickness in metres

F = 7500 # maxq fin force in Newtons
D = 2000 #maxq drag force on nosecone

def calcMassPerUnitLength(x,t):
  ## this function returns the mass per unit length in kg/m of the rocket at point x, measured from the base in m, and at time t in seconds
  total = 0
  # structure
  if (x<0.5):
    #engine
    total+= 20/0.5
  if (x<1.015):
    #fin can
    total+= 30/1.015
  if (x>1.015 and x<3.452):
    #bottom tank
    total+= 2700*np.pi*2*R*T_fuel
  if (x>3.452 and x<3.962):
    # aerocover - intertank
    total+= 2700*np.pi*2*R*T_aero_inter
  if (x>3.962 and x<5.999):
    #top tank
    total+= 2700*np.pi*2*R*T_ox
  if (x>5.999 and x<8.194):
    #top aerocover
    total+= 7800*np.pi*2*R*T_aero_top
  if (x>5.999 and x<6.289):
    #recovery system
    total+=12/0.29
  if (x>6.289 and x<8.194):
    #COPV
    total = 45/1.905
  if (x>8.194):
    #nosecone, tapered
    total += 7800*np.pi*2*R*0.5e-3*(1-((x-8.194)/1.446))

  # fuel
  if (x>1.015 and x<3.452):
    #bottom tank - fuel
    if (t<32):
      total+= 786 * np.pi * (R**2) * (1- (t/32)) * 0.9 #0.9 is a correction factor bc the tank is not completely cylindrical. Measurements take us to the ends including caps

  if (x>3.962 and x<5.999):
    #top tank
    if (t<32):
      total+= 1141 * np.pi * (R**2) * (1- (t/32)) * 0.9 #0.9 is a correction factor bc the tank is not completely cylindrical. Measurements take us to the ends including caps

  # other
  total += 25/9.64 #averaged distribution of the mass of the aerostructures
  total += 29/9.64 #averaged distribution of the plumbing system
  
  return total

def calcMass(t):
  ## this function returns the total mass of the craft at time t
  dx = 0.01
  x = 0
  mass = 0
  while (x<9.64):
    mass += dx*calcMassPerUnitLength(x,t)
    x += dx
  return mass

def calcCentreOfMass(t):
  ## this function calculates the centre of mass, returning the height of the CoM in metres from the bottom of the rocket
  dx = 0.01
  x = 0
  firstMoment = 0
  while (x<9.64):
    firstMoment += calcMassPerUnitLength(x,t)*dx*x
    x+=dx
  return firstMoment / calcMass(t)

##### MY FUNCTION: PLOTS STABILITY AND COP VS 2 CAL POINT AND PRINTS STABILITY AT TIME T #######

#cops from RASAero for mach 0,0.5,1.0 .... 5.0
def stability_check(cops,t,p):
    if len(cops) != 11:
        raise ValueError("cops input must be length 11, with cops from 0,0.5.... 5 mach from rasaero")
    #machs=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5] find from data sheet the approx time corresponding 5.5 will be extrapolated
    mach_to_times=[0.00,3.81,7.26,11.03,15.94,19.64,22.52,25.36,27.74,29.79,31.65] #corresponding
    coeffs=np.polyfit(mach_to_times,cops,p)
    eq=np.poly1d(coeffs)
    t_com=np.linspace(0,35,10*35)
    y_cop=eq(t_com)
    coms=[]
    for j in range(len(t_com)):
        coms.append((9.64-calcCentreOfMass(t_com[j]))*39.37)   #cop must be 2 cals below com
    calibers=(y_cop-coms)/(0.375*39.37)
    figure,axes1=plt.subplots(1,2)
    plt.tight_layout()
    axes1[0].plot(t_com,coms,color='red',label='COM')
    axes1[0].legend(loc='upper right')
    axes1[0].set_xlabel('Time(s)')
    axes1[0].set_ylabel('Distance from nose tip (inches)')
    axes1[0].plot(t_com,y_cop,color='green',label='C.O.P - ONLY VALID TO BLACK LINE')
    axes1[0].axvline(32.82, color='black', label='mach 5.5 timestamp')
    for i in range(0,len(cops)):
      axes1[0].plot(mach_to_times[i],cops[i],marker='o',markeredgecolor="yellow", markerfacecolor="purple")
    axes1[0].legend(loc='lower left')
    axes1[0].set_title('COP vs COM')
    if not 0<=t<=33:
      raise ValueError("time must be in range 0 to 33s")
    t_finder=round(10*t)
    stability_point=calibers[t_finder]
    print(f'Stability at time {round(t)} seconds is {stability_point} calibers.')
    axes1[1].plot(t_com,calibers,label='calibers of stability')
    axes1[1].axvline(32.82, color='black', label='mach 5.5/max speed time')
    axes1[1].set_xlabel('Time(s)')
    axes1[1].set_ylabel('Calibers of stability')
    axes1[1].legend(loc='upper right')
    plt.title(f'Stability Analysis',loc='center')
    plt.show()

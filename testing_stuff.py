from ambiance import Atmosphere
import numpy as np
import matplotlib.pyplot as plt
#atmosphere = Atmosphere([i for i in range(80000)])
#plt.plot(atmosphere.h, atmosphere.mean_particle_speed) #dont think this really is wind speed I want at all, although it somewhat varies as expected, but more on temp side
#plt.show()









'''h_list_l1 = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.25,2.5,3,3.5,4,4.5,5] 
h_list_t1 = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.25,2.5,3,3.5,4,5,6,7,8,12,18] 
u_ratio_list_l1 = [0,0.1*(10)**0.5,0.1*(11)**0.5,0.1*(15)**0.5,0.1*(21)**0.5,0.1*(29)**0.5,0.1*(32)**0.5,0.1*(16)**0.5,0.1*(19)**0.5,0.1*(17)**0.5,0.1*(18)**0.5,
                0.1*(23)**0.5,0.1*(32)**0.5,0.1*(41)**0.5,0.1*(55)**0.5,0.1*(61)**0.5,0.1*(68)**0.5,0.1*(76)**0.5,0.1*(86)**0.5,0.1*(90)**0.5,0.1*(95)**0.5,0.1*(99)**0.5,]
u_ratio_list_t1 = [0, 0.1*(12)**0.5,0.1*(13)**0.5,0.1*(16)**0.5,0.1*(19)**0.5,0.1*(27)**0.5,0.1*(30)**0.5,0.1*(31)**0.5,0.1*(33)**0.5,0.1*(35)**0.5,0.1*(37)**0.5,
                0.1*(39)**0.5,0.1*(45)**0.5,0.1*(49)**0.5,0.1*(49)**0.5,0.1*(50)**0.5,0.1*(52)**0.5,0.1*(54)**0.5,0.1*(56)**0.5,0.1*(59)**0.5,0.1*(63)**0.5,
                0.1*(66)**0.5,0.1*(72)**0.5,0.1*(75)**0.5,0.1*(85)**0.5,0.1*(98)**0.5,]
h_list_l2 = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.25,2.5,3,3.5,4,4.5] 
u_ratio_list_l2 = [(1/(0.1*np.sqrt(70)))*0.1*(2)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(3)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(3)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(4)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(5)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(6)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(8)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(9)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(10)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(14)**0.5,
                (1/(0.1*np.sqrt(70)))*0.1*(18)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(21)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(27)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(32)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(37)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(46)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(54)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(60)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(65)**0.5,(1/(0.1*np.sqrt(70)))*0.1*(70)**0.5]
h_list_l1 = [entry + 0.5 for entry in h_list_l1]
h_list_t1 = [entry + 0.5 for entry in h_list_t1]

plt.plot(h_list_l1, u_ratio_list_l1,  label = 'Laminar')
plt.plot(h_list_t1, u_ratio_list_t1, label = 'Turbulent')
plt.xlabel('Position from plate (mm)')
plt.ylabel('u/U')
plt.title('Boundary layer velocity to freestream velocity ratio against measurement position')
plt.legend()
plt.show()

plt.plot(h_list_l2, u_ratio_list_l2, label = 'Laminar')
plt.xlabel('Position from plate (mm)')
plt.ylabel('u/U')
plt.title('Boundary layer velocity to freestream velocity ratio against measurement position')
plt.legend()
plt.show()'''

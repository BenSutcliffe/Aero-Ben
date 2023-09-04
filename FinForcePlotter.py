import numpy as np
import matplotlib.pyplot as plt
import Classes
from Global_vars import *
from aero_coefficients import *
from forces import C_N_force, F_fin_N
from FlightProfileData import *

test_body = Classes.Bodyone 

#####
angle_attack_force_run = 3
start1 = 875    #should be above 875 as this is where mach > 1.2 so super sonic analysis works.
end1 = 4000
step1 = 5
####

def fin_F_array(angle_attack_force_run, start1, end1, step1):  #indexes of excel sheet
    f_list = []
    t_trunc_array = np.array(time_array[start1:end1:step1])
    for i in range(start1, end1, step1):
        beta1 = np.sqrt(abs((mach_array[i])**2 - 1))
        Normal_coeff1 = CNalphaN_super(N_fins, test_body.Arearef(), 0.315, beta1, angle_attack_force_run) #0.315 is area of fin currently. FORCES ONLY VALID FOR SUPERSONIC HERE
        Normal_coeff_alpha1 = C_N_force(Normal_coeff1, (angle_attack_force_run * np.pi/180))
        fin_force1 = F_fin_N(Normal_coeff_alpha1, density_array[i], test_body.Arearef(), vz_array[i])   #0 deg angle attack flight used here so only vz to consider.
        f_list.append(fin_force1)
    f_trunc_array = np.array(f_list)
    return t_trunc_array, f_trunc_array

t_plot, f_plot = fin_F_array(angle_attack_force_run, start1, end1, step1)

plt.plot(t_plot, f_plot/1000, label = 'Normal Force on Fin') #conversion to kN
plt.xlabel('Time(s)')
plt.ylabel('Total Fin force /kN')
plt.title(f'Angle of Attack is {angle_attack_force_run}')
plt.axvline(22, color = 'black', label = 'roughly Max Q')
plt.legend()
plt.show()
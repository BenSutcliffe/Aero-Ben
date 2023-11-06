import numpy as np
import matplotlib.pyplot as plt
import Classes
from Global_vars import *
from aero_coefficients import *
from forces import C_N_force, F_fin_N
from FlightProfileData import *

test_body = Classes.Bodyone

test_fins = Classes.Fin   #edit fin dimensions in Classes

#####
angle_attack_force_run = 3
start1 = 0   
end1 = 4500
step1 = 2
####

def fin_F_array(angle_attack_force_run, start1, end1, step1):  #indexes of excel sheet
    f_list = []
    cna = []
    angles = []
    t_trunc_array = np.array(time_array[start1:end1:step1])
    h_trunc_array = np.array(z_array[start1:end1:step1])
    for i in range(start1, end1, step1):
        if i>88:
            angle_attack_wind = (180/np.pi)*np.arctan(wind_lookup(z_array[i])/vz_array[i])
        else:
            angle_attack_wind = 0
        angles.append(angle_attack_wind)
        beta1 = np.sqrt(abs((mach_array[i])**2 - 1))
        if mach_array[i]<0.8:
            Normal_coeff1 = CNalphaN_subs(N_fins, test_fins.fin_span, test_body.Arearef(), test_fins.area(), beta1, test_fins.fin_gamma())
        elif 0.8 < mach_array[i] <1.2:
            Normal_coeff1 = CNalphaN_trans(N_fins, test_fins.fin_span, test_body.Arearef(), test_fins.area(), mach_array[i], test_fins.fin_gamma(), angle_attack_wind )
        elif mach_array[i] >= 1.2:
            Normal_coeff1 = CNalphaN_super(N_fins, test_body.Arearef(), test_fins.area(), beta1, angle_attack_wind) #FORCES ONLY VALID FOR SUPERSONIC HERE
        cna.append(Normal_coeff1)
        cn_force = C_N_force(Normal_coeff1, (angle_attack_wind * np.pi/180))
        fin_force1 = F_fin_N(cn_force, density_array[i] , test_fins.area(), vz_array[i])   #0 deg prelim flight used here so only vz to consider. #0.315
        f_list.append(fin_force1)
    f_trunc_array = np.array(f_list)
    return t_trunc_array, f_trunc_array, max(f_list), cna, h_trunc_array, angles

def fin_F_plotter():
    t_plot, f_plot, max_f, cna_plot, h_plot, ang_plot = fin_F_array(angle_attack_force_run, start1, end1, step1)
    print(f'Max Fin Force is {max_f/1000} kN, Fin area of {test_fins.area()}m^2')
    #print(f'Chord_root, fin_span, Chord_tip, sweep_length, body_radius: {test_fins.Chord_root(), test_fins.fin_span(), test_fins.Chord_tip(), test_fins.sweep_length, test_fins.body_radius()}')
    plt.plot(t_plot, f_plot/1000, label = 'Normal Force on Fin') #conversion to kN
    plt.xlabel('Time(s)')
    plt.ylabel('Total Fin force /kN')
    plt.title(f'Angle of Attack is {angle_attack_force_run} degrees (IGNORE)')
    plt.axvline(5.9, color = 'green', label = 'Transonic 0.8<M<1.2', linestyle = '--')
    plt.axvline(8.6, color = 'orange', label = 'Supersonic 1.2<M<5', linestyle = '--')
    plt.axvline(32.9, color = 'red', label = 'Hypersonic M>5', linestyle = '--')
    #plt.axvline(21.4, color = 'black', label = 'roughly Max Q', linestyle = '--')
    plt.ylim(0, (max_f+400)/1000)
    plt.legend()
    plt.show()
    #
    plt.plot(h_plot/1000, f_plot/1000, label = 'Normal Force on Fin') #conversion to kN
    plt.xlabel('Altitude (km)')
    plt.ylabel('Total Fin force /kN')
    plt.title(f'Angle of Attack is {angle_attack_force_run} degrees (IGNORE)')
    plt.ylim(0, (max_f+400)/1000)
    plt.legend()
    plt.show()
    plt.plot(t_plot[0:end1:1], cna_plot[0:end1:1], label = 'CNalpha per rad')
    mach_to_times1=[0.00,3.81,7.26,11.03,15.94,19.64,22.52,25.36,27.74] #,29.79,31.65]
    for i in range(0,len(mach_to_times1)):
      plt.axvline(mach_to_times1[i], color = 'red', label = f'Mach {i*0.5}', linestyle = 'dotted')
    plt.legend()
    plt.show()
    plt.plot(t_plot, ang_plot)
    plt.show()
    
def wind_lookup(alti):
    #multiple datasets. seems to vary wind vs altitude so much over a year and location
    #max launch wind speed of 5.8m/s
    p = 7
    alts = [0, 2, 5, 7, 10, 12, 15, 17, 20, 25, 30, 35, 40]
    alt_windspeed=[5.8, 25, 35, 55, 65, 45, 35, 25, 20, 21, 30, 40, 50] #corresponding to Spokane, WA autumn
    alt_windspeed=[5.8, 11, 15, 21, 25, 15, 11, 9, 8, 10, 11, 15, 25] #NL avg
    coeffic=np.polyfit(alts, alt_windspeed, p)
    equ = np.poly1d(coeffic)
    #plt.plot(alts, alt_windspeed, label = 'Wind data')
    test_alts = np.array(np.linspace(0,40000,100))
    test_wind = [1.5*equ(a/1000) for a in test_alts ]
    #plt.plot(test_alts/1000, test_wind, label = 'Curve fitted data + safety factor')
    #plt.ylabel('Wind (m/s)')
    #plt.xlabel('Altitude (km)')
    #plt.legend()
    #plt.show()
    wind_s = 1.5*equ(alti/1000)
    #print(wind_s)
    return wind_s
wind_lookup(24)
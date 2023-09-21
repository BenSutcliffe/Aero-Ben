import numpy as np
import matplotlib.pyplot as plt
from Classes import *
from FlightProfileData import *

####
Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 78e9, 1.1, 0.7, 0.35, 8e-3, 1e-3, 97.7, 150, 14.76, 6.25
# edit above as appropriate. 
thc = th - 2 * ths

startf, endf, stepf = 0, 3200, 1
####

def flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf, solf, compf, solm, compm):
    #ss, cr, ct, th, ths, thc = ss*39.37, cr*39.37, ct*39.37, th*39.37, ths*39.37, thc*39.37
    #Ge = Gs #* 0.000145038 #effective shear modulus. Unsure how actually behaves with sandwich panel behaviour.
    area = 0.5 * (cr + ct) * ss
    AR = ss**2 / area
    lam = ct/cr
    critMJ = []
    critmach_noncomp = []
    mach_f_array = np.array(mach_array[startf:endf:stepf])
    t_f_array = np.array(time_array[startf:endf:stepf])
    for j in range(startf, endf, stepf):
        X_flut = 39.3*AR**3 * 1/(th/cr)**3 * 1/(AR+2)
        critmachnoncomp_toadd = np.sqrt(Gs*0.000145038/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))
        critmach_noncomp.append(critmachnoncomp_toadd)
        critMJ_toadd = np.sqrt(Gs*0.000145038/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))*(compf/solf)*(np.sqrt(solm/compm))
        critMJ.append(critMJ_toadd)
    critMJ_array = np.array(critMJ)
    return mach_f_array, t_f_array, critMJ_array, critmach_noncomp

def flutt_plot(sf, sf2, sf_switch, noncomp_switch):
    mach_fplot, t_plotf, critMJ_plot, critmach_noncomp = flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf, solf, compf, solm, compm)
    print(f'{mach_fplot[0::2000]} read this to check mach values plot correctly')
    plt.plot(t_plotf, mach_fplot, label = 'Simulated actual Mach', color = 'red')
    if sf_switch == True:    
        plt.plot(t_plotf, mach_fplot*sf, label = f'Simulated with sf of {sf}', color = 'red', linestyle = 'dotted')
        plt.plot(t_plotf, critMJ_plot*sf2, label = f'Simulated with sf of {sf2}', color = 'blue', linestyle = 'dotted')
    if noncomp_switch == True:
        plt.plot(t_plotf, critmach_noncomp, label = 'Crit solid Mach', color = 'black')
    plt.plot(t_plotf, critMJ_plot, label = 'Critical Mach (NACA 4197)', color = 'blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Mach number')
    plt.legend()
    plt.show()
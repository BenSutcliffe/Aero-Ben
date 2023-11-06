import numpy as np
import matplotlib.pyplot as plt
from Classes import *
from FlightProfileData import *

####
Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 78e9, 1.1, 0.7, 0.35, 7e-3, 1e-3, 59.6, 70.8, 8.2, 5.97
Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 25e9, 0.65, 0.4, 0.5, 14e-3, 1e-3, 59.6, 70.8, 8.2, 5.97
Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 78e9, 1.0, 0.7, 0.325, 7e-3, 1e-3, 59.854, 83, 14.5, 5.87    
Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 78e9, 1.0, 0.7, 0.325, 7e-3, 1e-3, 97.945, 129.75, 14.5, 5.87 #bending
Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 78e9, 1.0, 0.7, 0.325, 9e-3, 1e-3, 153.4, 197, 14.6, 5.7    #torsion #323

Gs, cr, ct, ss, th, ths, solf, compf, solm, compm = 26.9e9, 0.75, 0.50, 0.40, 12e-3, 1e-3, 160, 185.6, 15.36, 5.6 #torsion freqs (edited for Al here)
# edit above as appropriate. 
thc = th - 2 * ths

startf, endf, stepf = 0,4000, 1
####

def flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf, solf, compf, solm, compm):
    #ss, cr, ct, th, ths, thc = ss*39.37, cr*39.37, ct*39.37, th*39.37, ths*39.37, thc*39.37
    #Ge = Gs #* 0.000145038 #effective shear modulus. Unsure how actually behaves with sandwich panel behaviour.
    area = 0.5 * (cr + ct) * ss
    AR = ss**2 / area
    lam = ct/cr
    critMJ = []
    critmach_noncomp = []
    critmach_noncomptaper = []
    mach_f_array = np.array(mach_array[startf:endf:stepf])
    t_f_array = np.array(time_array[startf:endf:stepf])
    for j in range(startf, endf, stepf):
        X_flut = 39.3*AR**3 * 1/(th/cr)**3 * 1/(AR+2)
        critmachnoncomp_toadd = np.sqrt(Gs*0.000145038/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))
        critmach_noncomp.append(critmachnoncomp_toadd)
        critmach_noncomptaper.append(critmachnoncomp_toadd*0.77)
        critMJ_toadd = np.sqrt(Gs*0.000145038/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))*(compf/solf)*(np.sqrt(solm/compm))
        critMJ.append(critMJ_toadd)
    critMJ_array = np.array(critMJ)
    return mach_f_array, t_f_array, critMJ_array, critmach_noncomp, critmach_noncomptaper

def flutt_plot(sf, sf2, sf_switch, noncomp_switch):
    mach_fplot, t_plotf, critMJ_plot, critmach_noncomp, critmach_noncomptaper = flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf, solf, compf, solm, compm)
    print(f'{mach_fplot[0::200]} read this to check mach values plot correctly')
    plt.plot(t_plotf, mach_fplot, label = 'Simulated actual Mach', color = 'red')
    if sf_switch == True:    
        plt.plot(t_plotf, mach_fplot*sf, label = f'Simulated with sf of {sf}', color = 'red', linestyle = 'dotted')
        #plt.plot(t_plotf, critMJ_plot*sf2, label = f'Simulated with sf of {sf2}', color = 'blue', linestyle = 'dotted')
    if noncomp_switch == True:
        plt.plot(t_plotf, critmach_noncomp, label = 'Crit solid Mach', color = 'black')
        plt.plot(t_plotf, critmach_noncomptaper, label = 'Crit solid Mach, taper experiment', color = 'black', linestyle = 'dotted')
    #plt.plot(t_plotf, critMJ_plot, label = 'Critical Mach (NACA 4197)', color = 'blue')
    #
    finsim_points = [2.25, 2.52, 2.83, 3.19, 3.62, 4.13, 4.75, 5.5] #flutter #difference in atmospheric model note.
    #finsim_points = [1.69, 1.89, 2.12, 2.39, 2.71, 3.1, 3.56, 4.12] # divergence
    finsim_ts = [0, 7.41, 11.52, 14.94, 17.77, 20.26, 22.45, 24.42 ] #this is to validate solid model analysis as a lower bound #naca 4197 composite correction is employed for other
    for i in range(0,len(finsim_points)):
        plt.plot(finsim_ts[i],finsim_points[i],marker='o',markeredgecolor="yellow", markerfacecolor="purple", label = f'{i*6000}ft altitude. Flutter V')
    print('Note that if fin design is changed, these points from FinSim need to be updated. This was just to ensure FinSim and code were in agreement for analysis on flutter')
    #
    plt.xlabel('Time (s)')
    plt.ylabel('Mach number')
    plt.ylim(0,10)
    plt.yticks(np.arange(0,10,0.5))
    plt.legend()
    plt.show()
    safety_plot = [critmach_noncomptaper[a]/mach_fplot[a] for a in range(len(critMJ_plot))]
    plt.plot(t_plotf[startf+500:endf-600:stepf], safety_plot[startf+500:endf-600:stepf])
    plt.title('Safety factor for taper simulating')
    plt.show()
    print(f'Safety check: Max mach number in array is: {max(mach_fplot)}')
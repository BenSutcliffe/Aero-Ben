import numpy as np
import matplotlib.pyplot as plt
from Classes import *
from FlightProfileData import *

Gs, cr, ct, ss, th, ths, thc = 78e9, 1.1, 0.7, 0.35, 12e-3, 1e-3, 10e-3

startf, endf, stepf = 0, 3800, 1

def flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf):
    #ss, cr, ct, th, ths, thc = ss*39.37, cr*39.37, ct*39.37, th*39.37, ths*39.37, thc*39.37
    Ge = Gs #* 0.000145038 #effective shear modulus. Unsure how actually behaves with sandwich panel behaviour.
    area = 0.5 * (cr + ct) * ss
    AR = ss**2 / area
    lam = ct/cr
    critMJerry = []
    mach_f_array = np.array(mach_array[startf:endf:stepf])
    t_f_array = np.array(time_array[startf:endf:stepf])
    for j in range(startf, endf, stepf):
        X_flut = 39.3*AR**3 * 1/(th/cr)**3 * 1/(AR+2)
        critMJ_toadd = np.sqrt(Ge*0.000145038/((pressure_array[j]/101325)*((lam+1)/2)*X_flut))
        critMJerry.append(critMJ_toadd)
    critMJ_array = np.array(critMJerry)
    return mach_f_array, t_f_array, critMJ_array

def flutt_plot(sf):
    mach_fplot, t_plotf, critMJ_plot = flutterer(Gs, cr, ct, ss, th, ths, thc, startf, endf, stepf)
    plt.plot(t_plotf, mach_fplot, label = 'Simulated actual Mach', color = 'red')
    plt.plot(t_plotf, mach_fplot*sf, label = 'Simulated with sf of {sf}', color = 'red', linestyle = 'dotted')
    plt.plot(t_plotf, critMJ_plot, label = 'Critical Mach (NACA 4197)', color = 'blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Mach number')
    plt.legend()
    plt.show()
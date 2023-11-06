from Stability_and_COMs import stability_check
from FinForcePlotter import fin_F_plotter
from flutter import *

####FIN NORMAL FORCE
fin_F_plotter()

####STABILITY
cops=[294.25,294.25,297.69,307.6,303.52,295.8,287.78,279.91,272.21,264.68,257.52]#array length 11 of rasaero cops from mach 0,0.5....5 (in inches as given in software)
cops = [330.42, 330.42, 337.42, 338.55, 325.53, 312.14, 301.45, 291.5, 280.14, 270.29, 261.29] #0.5 span
cops = [324.43, 324.43, 331.29, 333.11, 320.84, 307.83, 295.3, 283.5, 273.9, 263.29, 254.5] #0.45 span
cops = [303.44, 303.44, 308.29, 313.12, 309.73, 301.29, 292.4, 282.89, 274.29, 265.94, 257.69] #0.35 span clipped delta, 0.9,0.35,0.6
cops = [295.31, 295.31, 299.79, 302.77, 304.11, 298.02, 290.32, 282.27, 274.2, 266.15, 258.71] #0.325 span, 1.0, 0.325, 0.7
cops = [312.09, 312.09, 318.89, 323.00, 313.87, 302.67, 292.16, 281.96, 272.33, 263.15, 254.56] #0.65,0.45 span, 0.45 tip, clipped delta
#rocket body length should be 9.64m total in rasaero ii
cops = [315.75, 315.75, 321.55, 327.07, 317.72, 306.62, 295.27, 284.69, 275.28, 265.59, 257.52] #0.75, 0.5, 0.4 span.
cops = [312.09, 312.09, 318.89, 323.00, 313.87, 302.67, 292.16, 281.96, 272.33, 263.15, 254.56] #same but now corrected to 9.64m length

t=32.8                                                                            #choose t to also find stability value at time t printed in terminal
p=3                                                                               #degree of polynomial to fit COPs to. needs to accurately extrapolate from mach 5 to 5.5

stability_check(cops,t,p)
####

####FLUTTER    
noncomp_switch = True
sf_switch = True    #Change to turn safety factor line plots on and off. edit fin dimensions and stuff in flutter file.
sf = 1.2              #safety factor for sim
sf2 = 0.8             #sf multiplier for crit

print(f'Skin Shear Modulus: {Gs/1e9}GPa, Root chord of {cr}m, Tip chord of {ct}m, Fin Span of {ss}m, Thickness of {th}m, Skin thickness of {ths}m, Core thickness of {thc}m, composite mass of {compm}, freqs are sol {solf} and comp {compf} Hz')
flutt_plot(sf, sf2, sf_switch, noncomp_switch)
####
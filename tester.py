from Stability_and_COMs import stability_check
from FinForcePlotter import fin_F_plotter

fin_F_plotter()

cops=[294.27,294.27,297.81,307.58,303.29,295.7,287.87,279.97,272.15,264.73,257.55] #array length 11 of rasaero cops from mach 0,0.5....5 (in inches as given in software)
t=32.6 #choose t to also find stability value at time t printed in terminal #markers are actual COP points to compare to graph fit
p=5    #degree of polynomial to fit COPs to. 2 is usually best. it needs to accurately extrapolate from mach 5 to 5.5
stability_check(cops,t,p) 
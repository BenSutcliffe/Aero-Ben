"""
Body flight profile critical values
"""
import numpy as np
"""
Taken from Henry Free's preliminary design document - Flight parameters
"""
speed_sound = 295 #speed of sound

start_mass = 632 #Wet mass, kg
end_mass = 208 #Recovery Mass, kg
v_burnout = 1588.34 #Burnout velocity, m/s
max_q_velo = 841.079701 #Velocity at Max-Q, m/s
max_q_rho = 0.403219 #Density at Max-Q, kg/m3
max_q_staticp = 25687.78 #Static pressure at Max-Q, Pa
p_atm = 94321.68 #Static pressure at launch, Pa
max_q_Mach = max_q_velo/speed_sound
max_q_beta = np.sqrt(abs(max_q_Mach**2 - 1))

"""
Taken from Henry Free's preliminary design document - Geometry parameters, m
"""
Nosecone_length = 1.775 #Nosecone length
Body_dia = 0.375 #body diameter
Body_len = 7.865 #body tube length
CoM = 6.10 #for Griffin

"""
Derived variables - Geometry m
"""
total_length = Body_len+Nosecone_length
fineness = total_length/Body_dia


"""
Material Properties
"""
#G_alu = 24E9 #Shear Modulus Aluminium, Pa
#G_alu_psi = 3.7e6 #Shear Modulus Aluminium, Psi
#density_alu = 2710 #Density Aluminium, kg/m3

G_alu = 79.3E9 #Shear Modulus Aluminium, Pa
G_alu_psi = 11.5e6 #Shear Modulus Aluminium, Psi
density_alu = 7850 #Density Aluminium, kg/m3 (already edited for steel here)
"""
Simlation variables - Physical
"""
Roughness =3e-6 #body surface roughness - corresponding to a painted surface
N_fins = 4 #number of rocket fins
angle_attack = 0 #angle of attack for simulation of stability
angle_attack_force = 3 #angle of attack for simulation of stability, cannot be equal to zero
desired_stability = 2.5

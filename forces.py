"""
Functions describing fin forces
"""

def C_N_force(C_N_alpha, angle_attack):
    """
    Returns the angle dependent normal force coefficient for a finset and angle of attack

    Parameters
    ----------
    C_N_alpha : float
      finset normal force coefficent
    angle_attack : float
      angle of attack of the fins
      
    Returns
    -------
    C_N : float
      angle dependent normal force coefficient
    """
    C_N = C_N_alpha*angle_attack
    return C_N

def F_fin_N(C_N, density, Area_fin, velocity):
    """
    Returns the restoring force produced by a finset at a given angle of attack
    Parameters
    ----------
    C_N : float
      finset normal force coefficent, dependent on angle of attack
    density : float
      atmospheric density at desired point
    Area_fin : float
      area of one side of the fin

    Returns
    -------
    force_fin : float
      the restoring force produced by the fins at a given angle of attack
    """
    force_fin = 0.5 * C_N * density * Area_fin * (velocity**2)
    return force_fin
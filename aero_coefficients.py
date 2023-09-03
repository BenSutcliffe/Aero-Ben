"""
Functions describing fin stability
"""

import numpy as np
from scipy.integrate import quad

def CNalphaN_subs(num_fin, fin_span, Area_ref, Area_fin, Beta, mid_chord_gamma):
  """
    Computes the normal force coefficient for all the fins in the subsonic regime, M<0.8.
    Barrowman analysis

    Parameters
    ----------
    num_fin : float
      number of fins on the rocket
    fin_span : float
      fin span height, distance from root to tip
    Area_ref: float
      cross sectional reference area for the rocket body
    Area_fin: float
      fin planar side area
    Beta: float
      root(Machno^2 - 1), inverse of Prandtl number
    mid_chord_gamma: float
      angle between the two midchord positions of the fins
      
    Returns
    -------
    CNalphaN: float
      value of the normal force coefficient of the fins in subsonic regime
  """
  CNalphaN = (num_fin/2) * (2 * np.pi) * (((fin_span)**2) /Area_ref)/(1 + np.sqrt(1 + ((Beta * (fin_span)**2)/(Area_fin * np.cos(mid_chord_gamma)))**2))
  return CNalphaN

def CNalphaN_super(num_fin, Area_ref, Area_fin, Beta, angle_attack):
  """
    Computes the normal force coefficient for all the fins in the supersonic regime M>1.2 based
    on Busemann theory.

    Parameters
    ----------
    num_fin : float
      number of fins on the rocket
    Area_ref: float
      cross sectional reference area for the rocket body
    Area_fin: float
      fin planar side area
    Beta: float
      root(Machno^2 - 1), inverse of Prandtl number
    angle_attack: float
      angle of attack of the vehicle
      
    Returns
    -------
    CNalphaN: float
      value of the normal force coefficient of the fins in supersonic regime
  """
  #Computes the Mach value corresponding with beta
  M_value = np.sqrt(np.abs(1-(Beta)**2))

  #Finds the values for the three velocity dependent coefficients
  K_1 = 2/Beta 
  K_2 = (((2.4*M_value**4)-(4*Beta**2))/(4*Beta**4))
  K_3 = (((2.4*M_value**8)-(10.88*M_value**6)+(24*M_value**4)+(8))/(6*Beta**7))

  #Finds the values for the force coefficient using the above coefficients and angle of attack
  CNalphaN = (num_fin/2) * (Area_fin/Area_ref) * ((K_1) + (K_2 * angle_attack * np.pi/180) + (K_3 * (angle_attack * np.pi/180)**2)) 
  return CNalphaN

def CNalphaN_trans(num_fin, fin_span, Area_ref, Area_fin, Mach_no, mid_chord_gamma, angle_attack):
  """
    Linearly interpolates normal force coefficient for the fins for 0.8<M<1.2

    Parameters
    ----------
    num_fin : float
      number of fins on the rocket
    fin_span : float
      fin span height, distance from root to tip
    Area_ref: float
      cross sectional reference area for the rocket body
    Area_fin: float
      fin planar side area
    Mach_no: float
      Mach number of the vehicle
    mid_chord_gamma: float
      angle between the two midchord positions of the fins
      
    Returns
    -------
    CNalphaN: float
      value of the normal force coefficient of the fins in transsonic regime
  """
  beta_sub = 0.6 #Value of inverse of Prandtl number for M=0.8
  beta_super = 0.6633
  CNalphaNpoint8 = CNalphaN_subs(num_fin, fin_span, Area_ref, Area_fin, beta_sub, mid_chord_gamma)
  CNalphaNonetwo = CNalphaN_super(num_fin, Area_ref, Area_fin, beta_super, angle_attack)
  CNalphaN = CNalphaNpoint8 + ((CNalphaNonetwo-CNalphaNpoint8)*((Mach_no-0.8)/(0.4)))
  return CNalphaN

def C_N_body(Area_plan, Area_ref, angle_attack, K=1.1):
  """
    Returns the normal force coefficient for the body tube

    Parameters
    ----------
    Area_plan : float
      side area of the body
    Area_ref: float
      cross sectional reference area for the rocket body
    Area_fin: float
      fin planar side area
    angle_attack: float
      angle of attack of the vehicle
    K:
      constant scalar term
      
    Returns
    -------
    CNalphaN: float
      value of the normal force coefficient of the body tube
  """
  CNalphaN = K * Area_plan/Area_ref * (np.sin(np.pi*angle_attack/180))**2
  return CNalphaN

def X_N(nose_height, body_height):
  """
    Returns the centre of pressure of the body tube relative to the top of the nosecone

    Parameters
    ----------
    nose_height : float
      height of the nosecone
    body_height: float
      height of the body tube

      
    Returns
    -------
    CP_bodytube: float
      vertical position of the centre of pressure of the body tube relative to the top of the nosecone
  """
  CP_bodytube = body_height/2 + nose_height #Adds half the height to the nosecone length
  return CP_bodytube

def Xf_supersonic(MAC_length, fin_span, Area_fin, Beta):
  """
    Returns the centre of pressure of the fins relative to their leading point for the supersonic regime, Fleeman E. - Tactical 
    Missile Design

    Parameters
    ----------
    MAC_length : float
      length of the fin Mean Aerodynamic Chord
    fin_span : float
      fin span height, distance from root to tip
    Area_fin: float
      fin planar side area
    Beta: float
      root(Machno^2 - 1), inverse of Prandtl number

      
    Returns
    -------
    Cp_x_distance : float
      distance between the top of the fin and centre of pressure for supersonic regime
  """
  Aspect_ratio2 = 2*(fin_span)**2 / Area_fin #Calculates the fin aspect ratio
  Cp_x_distance = MAC_length * (((Aspect_ratio2 * Beta) - 0.67)/((2*Aspect_ratio2*Beta) - 1))
  return Cp_x_distance

def chord_sq(y_dist, Fins):
  """
    Gives the square of fin chord length by distance away from the fin root

    Parameters
    ----------
    y_dist : float
      distance from fin root
    Fins : Class
      Fin object


      
    Returns
    -------
    chord_square : float
      gives the length of the fin chord at a given y_dist
  """
  chord_square = (Fins.Chord_root + ((Fins.Chord_tip - Fins.Chord_root)*y_dist)/Fins.fin_span)**2
  return chord_square

def MAC_length(Fins, chord_function):
  """
    Returns the length of the Mean Aerodynamic Chord

    Parameters
    ----------
    Fins : float
      Fin object
    chord_function: function
      function describes how square of the fin chord length varies with distance from the root

    Returns
    -------
    Mac_length : float
      length of the Mean Aerodynamic Chord
  """
  result, err = quad(chord_function, 0, Fins.fin_span, args=(Fins,))
  Mac_length = result/(Fins.area())
  return Mac_length

def c_LE(y_dist, Fins):
    """
    Returns the length of the Mean Aerodynamic Chord

    Parameters
    ----------
    y_dist : float
      distance from fin root
    Fins : Class
      Fin object

    Returns
    -------
    leadingedge_chordlength_product : float
      returns the chord length x distance to front of the fin for a given distance from the root chord to a point on the fin
  """
    leadingedge_chordlength_product = (Fins.Chord_root + ((Fins.Chord_tip - Fins.Chord_root)*y_dist)/Fins.fin_span)*((Fins.Chord_root - Fins.Chord_tip)*y_dist/Fins.fin_span)
    return leadingedge_chordlength_product

def MAC_x_distance(Fins, chord_le_function):
  """
    Returns the vertical distance from the leading edge at the top of the MAC to the top point of the fin

    Parameters
    ----------
    Fins : float
      Fin object
    chord_le_function : function
      function product of the fin chord length and sweep length at a given span position

    Returns
    -------
    Mac_x_dist : float
      vertical distance from the leading edge at the top of the MAC to the top point of the fin
  """
  result, err = quad(chord_le_function, 0, Fins.fin_span, args=(Fins,))
  Mac_x_dist = result/(Fins.area())
  return Mac_x_dist

def Xf_transonic(MAC_length, fin_span, Area_fin, Mach_no):
  """
    Returns the vertical distance from the leading edge at the top of the MAC to the top point of the fin

    Parameters
    ----------
    MAC_length : float
      length of fin mean aerodynamic chord
    fin_span : float
      fin span height, distance from root to tip
    Area_fin: float
      fin planar side area
    Mach_no: float
      Mach number of the vehicle

    Returns
    -------
    Mac_x_dist : float
      vertical distance from the leading edge at the top of the MAC to the top point of the fin
  """
  #calculate supersonic fin position at mach 2
  f_1 = Xf_supersonic(MAC_length, fin_span, Area_fin, 1.732)/MAC_length

  #calculate gradient of supersonic fin position function at mach 2
  dB = 1e-2
  beta_1 = np.sqrt(np.abs((2+dB)**2 - 1)) 
  beta_2 = np.sqrt(np.abs((2-dB)**2 - 1))
  f_2 = (Xf_supersonic(MAC_length, fin_span, Area_fin, (beta_1))/MAC_length  - Xf_supersonic(MAC_length, fin_span, Area_fin, (beta_2))/MAC_length)/(2*dB)

  #matrix solver method to fit a 5th order polynomial
  a = np.array([[1/32, 1/16, 1/8, 1/4, 1/2, 1], [5/16, 1/2, 3/4, 1, 1, 0], [32, 16, 8, 4, 2, 1], [80, 32, 12, 4, 1, 0], [160, 48, 12, 2, 0, 0], [240, 48, 6, 0, 0, 0]])
  b = np.array([0.25, 0, f_1, f_2,  0, 0])
  x = np.linalg.solve(a, b)
  value = ((x[0] * (Mach_no**5)) + (x[1] * (Mach_no**4)) + (x[2] * (Mach_no**3)) + (x[3] * (Mach_no**2)) + (x[4] * (Mach_no)) + (x[5]))*MAC_length
  return value
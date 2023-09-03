"""
Body component classes
"""

from operator import length_hint
from Global_vars import *
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.widgets import Slider

class Fins:
  """
  A class to represent a fin. All units to be in m.
  ...

  Attributes
  ----------
    Chord_root : float
      length of fin root chord
    fin_span : float
      height/span of the fin
    Chord_root : float
      length of fin tip chord
    sweep_length : float
      vertical distance between the top of the root chord and tip chord
    body_radius : float
      radius of the body the fins are attached to


  Methods
  -------
  MAC_y():
    Prints the spanwise distance between the root chord and the Mean Aerodynamic Chord.
  fin_gamma():
    Prints the angle between root chord midpoint and tip chord midpoint
  X_f():
    Prints the position of the centre of pressure of the fin in the subsonic regime. Length measured with respect to
    the top point on the fin.
  area():
    Prints the fin area
  K():
    Prints the fin interference factor
  """
  def __init__(self, Chord_root, fin_span, Chord_tip, sweep_length, body_radius):
    """
      Constructs all the necessary attributes for the fin object.

      Parameters
      ----------
      Chord_root : float
        length of fin root chord
      fin_span : float
        height/span of the fin
      Chord_root : float
        length of fin tip chord
      sweep_length : float
        vertical distance between the top of the root chord and tip chord
      body_radius : float
        radius of the body the fins are attached to
      gamma : float
        angle between root chord midpoint and tip chord midpoint
    """
    self.Chord_root = Chord_root
    self.fin_span = fin_span
    self.Chord_tip = Chord_tip
    self.sweep_length = sweep_length
    self.body_radius = body_radius

  def MAC_y(self):
    """
      Returns the spanwise distance between the root chord and the Mean Aerodynamic Chord.

      Employs the Barrowman Results.

      Returns
      -------
        MAC_y_distance : float
          distance between the root chord and the Mean Aerodynamic Chord
    """
    MAC_y_distance = (self.fin_span/3)*((self.Chord_root + (2*self.Chord_tip))/(self.Chord_root + self.Chord_tip))
    return MAC_y_distance

  def fin_gamma(self):
    """
      Returns the angle between root chord midpoint and tip chord midpoint.

      Employs the Barrowman Results.

      Returns
      -------
        gamma_angle : float
          angle between root chord midpoint and tip chord midpoint
    """
    gamma_angle = np.arctan(0.5*(self.Chord_root - self.Chord_tip)/self.fin_span)
    return gamma_angle

  def X_f(self):
    """
        Returns the position of the centre of pressure of the fin in the subsonic regime. Length measured with respect to
        the top point on the fin.

        Employs the Barrowman Results.

        Returns
        -------
          Cp_x_distance : float
            distance between the top of the fin and centre of pressure for subsonic regime
    """
    Cp_x_distance = ((self.sweep_length /3)*((self.Chord_root + (2*self.Chord_tip))/(self.Chord_root + self.Chord_tip))) + (1/6 * (((self.Chord_root)**2 + (self.Chord_tip)**2 + (self.Chord_root * self.Chord_tip))/(self.Chord_root + self.Chord_tip)))
    return Cp_x_distance

  def area(self):
    """
      Returns the area of one side of the fin

      Returns
      -------
        Fin_area : float
          fin area (one side)
    """
    Fin_area = 0.5 * self.fin_span * (self.Chord_root + self.Chord_tip)
    return Fin_area
  
  def K(self):
    """
      Returns fin interference factor due to the radius of the rocket body

      Returns
      -------
        fin_K_interference : float
          body -> fin interference term
    """
    fin_K_interference = 1 + (0.5*self.body_radius)/(self.fin_span + (0.5*self.body_radius))
    return fin_K_interference

class Body:
  """
  A class to represent the rocket body tube. All units to be in m.
  ...

  Attributes
  ----------
    body_diameter : float
      diameter of the rocket body
    body_height : float
      height of the rocket body tube (without nosecone)
    nosecone_height : float
      height of the nosecone

  Methods
  -------
  Arearef():
    Prints the cross sectional area of the body.
  areat():
    Prints the side projected planar area of the body
  """
  def __init__(self, body_diameter, body_height):
    """
        Constructs all the necessary attributes for the body object.

        Parameters
        ----------
        body_diameter : float
          diameter of the rocket body
        body_height : float
          height of the rocket body tube (without nosecone)
    """
    self.body_diameter = body_diameter
    self.body_height = body_height

  def Arearef(self):
    """
      Returns the cross sectional area of the body

      Returns
      -------
        cross_section_area : float
          cross sectional body area
    """
    cross_section_area = np.pi * (self.body_diameter**2)/4
    return cross_section_area

  def areat(self):
    """
      Returns the side projected planar area of the body

      Returns
      -------
        side_plane_area : float
          side plane projected body area
    """
    side_plane_area = self.body_diameter * self.body_height
    return side_plane_area


class Nosecone:
  """
    A class to represent the rocket body tube. All units to be in m.
    ...

    Attributes
    ----------
      nose_height : float
        diameter of the rocket body

    Methods
    -------
    Arearef():
      Prints the cross sectional area of the body.
    areat():
      Prints the side projected planar area of the body
  """
  def __init__(self, nose_height):
    """
      Constructs all the necessary attributes for the body object.

      Parameters
      ----------
      nose_height : float
        diameter of the rocket body
    """
    self.nose_height = nose_height
    self.CombinedC = 2
    
  def X_f(self):
    """
    Returns the distance between the top of the nosecone and the centre of pressure

    Returns
    -------
      Cp_x_distance : float
        distance between the top of the nosecone and the centre of pressure
    """
    Cp_x_distance = 0.666 * self.nose_height
    return Cp_x_distance

  def C_N(self):
    """
    Returns the normal force coefficient for the nosecone
    Returns
    -------
      C_N_nose : float
        normal force coefficient for the nosecone
    """
    C_N_nose = 2
    return C_N_nose

#Initialises the known classes for the rocket (not the fins)
Bodyone = Body(Body_dia, Body_len)
Cone = Nosecone(Nosecone_length)
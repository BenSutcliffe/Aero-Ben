#ignore this file also. both are not functioning properly atm.

def static_air_temperature(altitude):
    if altitude < 0:
        raise ValueError("Altitude must be non-negative.")
    elif altitude <= 11000:
        # Troposphere (up to 11 km)
        base_altitude = 0.0  # Sea level altitude in meters
        base_temperature = 288.15  # Sea level standard temperature in Kelvin
        lapse_rate = -0.00649  # Temperature lapse rate in Kelvin per meter
    elif altitude <= 20000:
        # Lower Stratosphere (11 km to 20 km)
        base_altitude = 11000.0  # Altitude at the start of the lower stratosphere
        base_temperature = 216.65  # Temperature at the start of the lower stratosphere in Kelvin
        lapse_rate = 0.001  # Temperature lapse rate in Kelvin per meter
    elif altitude <= 32000:
        # Upper Stratosphere (20 km to 32 km)
        base_altitude = 20000.0  # Altitude at the start of the upper stratosphere
        base_temperature = 216.65  # Temperature at the start of the upper stratosphere in Kelvin
        lapse_rate = 0.0028  # Temperature lapse rate in Kelvin per meter
    elif altitude <= 47000:
        # Mesosphere (32 km to 47 km)
        base_altitude = 32000.0  # Altitude at the start of the mesosphere
        base_temperature = 228.65  # Temperature at the start of the mesosphere in Kelvin
        lapse_rate = 0.002  # Temperature lapse rate in Kelvin per meter
    elif altitude <= 51000:
        # Lower Thermosphere (47 km to 51 km)
        base_altitude = 47000.0  # Altitude at the start of the lower thermosphere
        base_temperature = 270.65  # Temperature at the start of the lower thermosphere in Kelvin
        lapse_rate = 0.0015  # Temperature lapse rate in Kelvin per meter
    elif altitude <= 71000:
        # Upper Thermosphere (51 km to 71 km)
        base_altitude = 51000.0  # Altitude at the start of the upper thermosphere
        base_temperature = 270.65  # Temperature at the start of the upper thermosphere in Kelvin
        lapse_rate = 0.001  # Temperature lapse rate in Kelvin per meter
    elif altitude <= 85000:
        # Exosphere (71 km to 85 km)
        base_altitude = 71000.0  # Altitude at the start of the exosphere
        base_temperature = 214.65  # Temperature at the start of the exosphere in Kelvin
        lapse_rate = 0.0001  # Temperature lapse rate in Kelvin per meter
    else:
        # Above the exosphere (beyond 85 km)
        base_altitude = 85000.0
        base_temperature = 186.946  # Temperature at 100 km in Kelvin
        lapse_rate = 0.0001

    # Calculate the static temperature
    static_temperature_kelvin = base_temperature + lapse_rate * (altitude - base_altitude)

    return static_temperature_kelvin

def Ttcalc(mach, altitude):
    gamma = 1.4
    Tstat = static_air_temperature(altitude)
    Tt = Tstat * (1 + (mach**2)*(gamma-1)/2)
    print(f"Stagnation total temperature for a calorically perfect gas (generally higher estimate than imperfect) at {mach} Mach and {altitude} metres is {Tt} Kelvin")

    
Ttcalc(5.5,23200)
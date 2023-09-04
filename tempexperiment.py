#highly experimental code - do not trust it at all

import tkinter as tk
import math

class MachCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mach, Static, and Total Temperature Calculator")

        self.gama = 1.4
        self.alt = 0.0  # Altitude in meters
        self.mach = 2.0  # Initial Mach number
        self.temp_static = 288.15  # Initial static temperature in Kelvin (15°C)
        self.temp_total = 288.15  # Initial total temperature in Kelvin (15°C)
        self.rgas = 287.05  # Specific gas constant for dry air in J/(kg*K)
        self.rho0 = 1.225  # Sea level air density in kg/m^3
        self.rho = self.rho0

        self.create_widgets()

    def create_widgets(self):
        self.label_altitude = tk.Label(self.root, text="Altitude (meters):")
        self.label_altitude.grid(row=0, column=0)

        self.altitude_entry = tk.Entry(self.root)
        self.altitude_entry.grid(row=0, column=1)
        self.altitude_entry.insert(0, str(self.alt))
        self.altitude_entry.bind("<FocusOut>", self.update_altitude)

        self.label_mach = tk.Label(self.root, text="Mach Number:")
        self.label_mach.grid(row=1, column=0)

        self.mach_entry = tk.Entry(self.root)
        self.mach_entry.grid(row=1, column=1)
        self.mach_entry.insert(0, str(self.mach))
        self.mach_entry.bind("<FocusOut>", self.update_mach)

        self.compute_button = tk.Button(self.root, text="COMPUTE", command=self.compute_temperature)
        self.compute_button.grid(row=2, column=0, columnspan=2)
        self.compute_button.config(bg="red", fg="white")

        self.label_static_temperature_kelvin = tk.Label(self.root, text="Static Temperature (Kelvin):")
        self.label_static_temperature_kelvin.grid(row=3, column=0, columnspan=2)

        self.static_temperature_kelvin_label = tk.Label(self.root, text=str(self.temp_static))
        self.static_temperature_kelvin_label.grid(row=3, column=2)

        self.label_total_temperature_kelvin = tk.Label(self.root, text="Total Temperature (Kelvin):")
        self.label_total_temperature_kelvin.grid(row=4, column=0, columnspan=2)

        self.total_temperature_kelvin_label = tk.Label(self.root, text=str(self.temp_total))
        self.total_temperature_kelvin_label.grid(row=4, column=2)

    def update_altitude(self, event):
        try:
            self.alt = float(self.altitude_entry.get())
            self.compute_temperature()
        except ValueError:
            pass

    def update_mach(self, event):
        try:
            self.mach = float(self.mach_entry.get())
            self.compute_temperature()
        except ValueError:
            pass

    def compute_temperature(self):
        # Calculate static temperature based on altitude in meters
        self.temp_static = 288.15 - 0.0065 * self.alt
        self.temp_static = self.temp_static if self.alt <= 11000 else 216.65
        self.temp_static = self.temp_static + 1.0 * (self.alt - 11000) / 1000 if 11000 < self.alt <= 20000 else self.temp_static

        # Calculate total temperature based on static temperature and Mach number
        self.temp_total = self.temp_static * (1.0 + (self.gama - 1.0) * self.mach ** 2)

        # Display static temperature and total temperature in Kelvin
        self.static_temperature_kelvin_label.config(text=f"{self.temp_static:.2f} K")
        self.total_temperature_kelvin_label.config(text=f"{self.temp_total:.2f} K")


if __name__ == "__main__":
    root = tk.Tk()
    app = MachCalculator(root)
    root.mainloop()
import numpy as np
import matplotlib.pyplot as plt
from freefall_object import Freefall_object
from planets import Planet

class FreefallPlotter:
    def __init__(self, falling_object: Freefall_object, planet: Planet, num_points: int = 100):
        self.falling_object = falling_object
        self.planet = planet
        self.num_points = num_points

    def generate_time_array(self):
        collision_time = self.falling_object.analytical_collision_time(
            self.planet.air_density, self.planet.gravity
        )
        return np.linspace(0, collision_time, self.num_points)

    def generate_height_array(self, time_array):
        return [
            self.falling_object.analytical_height(self.planet.air_density, self.planet.gravity, t)
            for t in time_array
        ]

    def generate_velocity_array(self, time_array):
        return [
            self.falling_object.analytical_velocity(self.planet.air_density, self.planet.gravity, t)
            for t in time_array
        ]

    def plot_freefall(self, ax1, ax2):
        time_array = self.generate_time_array()
        height_array = self.generate_height_array(time_array)
        velocity_array = self.generate_velocity_array(time_array)

        # Plot height on the primary axis (ax1)
        color = 'tab:red'
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Height (m)', color=color)
        ax1.plot(time_array, height_array, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        # Plot velocity on the secondary axis (ax2)
        color = 'tab:blue'
        ax2.set_ylabel('Velocity (m/s)', color=color)
        ax2.plot(time_array, velocity_array, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

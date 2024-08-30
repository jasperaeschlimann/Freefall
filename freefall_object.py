import math

class Freefall_object:
    def __init__(self, name: str, start_height: float, start_velocity: float, drag_coefficient: float, mass: float, cross_sectional_area: float):
        """
        Initialise a Planet object.

        :param name: The name of the planet.
        :param start_height: The start height of the falling object (in m)
        :param start_velocity: The start velocity of the falling object (in m/s)
        :param drag_coefficient: The drag coefficient of the falling object
        :param mass: The mass of the falling object (in kg)
        :param cross_sectional_area: The cross sectional area of the falling object (in m^2)
        """
        self.name = name
        self.start_height = start_height
        self.start_velocity = start_velocity
        self.drag_coefficient = drag_coefficient
        self.mass = mass
        self.cross_sectional_area = cross_sectional_area


    def __repr__(self):
        return f"Freefall_object(name={self.name}, height={self.start_height} m, velocity={self.start_velocity} m/s, drag_coefficient={self.drag_coefficient}, mass={self.mass} kg, cross_sectional_area={self.cross_sectional_area} m^2)"
    

    def calculate_drag_constant(self, air_density: float) -> float:
            """
            Calculate the drag constant for the object based on the air density, drag coefficient, and cross sectional area.

            :param air_density: The air density in the environment (in kg/m^3)
            :return: The drag constant
            """
            return 0.5 * air_density * self.drag_coefficient*self.cross_sectional_area
    

    def analytical_collision_time(self, air_density: float, gravity: float) -> float:
            """
            Calculate the collision time of the falling object based on an analytical approach.

            :param air_density: The air density in the environment (in kg/m^3)
            :param gravity: The gravity of the planet into which the object is falling (in m/s^2)
            :return: The analytical prediction for the collision time
            """
            drag_constant = self.calculate_drag_constant(air_density)
            return math.acosh(math.exp((self.start_height*drag_constant)/self.mass))/math.sqrt((drag_constant*gravity)/self.mass)
    

    def analytical_height(self, air_density: float, gravity: float, time: float) -> float:
            """
            Calculate the height of the falling object at a time based on an analytical approach.

            :param air_density: The air density in the environment (in kg/m^3)
            :param gravity: The gravity of the planet into which the object is falling (in m/s^2)
            :return: The analytical prediction for the height at the time
            """
            drag_constant = self.calculate_drag_constant(air_density)
            return self.start_height-(self.mass/drag_constant)*(math.log(math.cosh(math.sqrt((drag_constant*gravity)/self.mass)*time)))
    

    def analytical_velocity(self, air_density: float, gravity: float, time: float) -> float:
            """
            Calculate the velocity of the falling object at a time based on an analytical approach.

            :param air_density: The air density in the environment (in kg/m^3)
            :param gravity: The gravity of the planet into which the object is falling (in m/s^2)
            :return: The analytical prediction for the velocity at the time
            """
            drag_constant = self.calculate_drag_constant(air_density)
            return -math.sqrt(self.mass*gravity/drag_constant)*math.tanh(math.sqrt(drag_constant*gravity/self.mass)*time)


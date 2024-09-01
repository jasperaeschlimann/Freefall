class Planet:
    def __init__(self, name: str, gravity: float, air_density: float):
        """
        Initialise a Planet object.

        :param name: The name of the planet.
        :param gravity: The gravitational acceleration on the planet (in m/s^2)
        :param air_density: The air density at the surface of the planet (in kg/m^3)
        """
        self.name = name
        self.gravity = gravity
        self.air_density = air_density

    def __repr__(self):
        return f"Planet(name={self.name}, gravity={self.gravity} m/s^2, air_density={self.air_density} kg/m^3)"

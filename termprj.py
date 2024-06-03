import math

class Rocket:
    def __init__(self, height, weight, width, thrust):
        self.height = height
        self.weight = weight
        self.width = width
        self.thrust = thrust  # in Newtons

    def __repr__(self):
        return f"Rocket(height={self.height}, weight={self.weight}, width={self.width}, thrust={self.thrust})"

    def calculate_escape_velocity(self, planet_mass, planet_radius):
        G = 6.67 * 10 ** -11  # gravitational constant
        escape_velocity = math.sqrt((2 * G * planet_mass) / planet_radius)
        return escape_velocity

    def calculate_final_velocity(self, planet_mass):
        # Basic rocket equation: Delta V = Isp * g * ln(m0/mf)
        # For simplicity, assume constant specific impulse and average mass
        g = 9.81  # Earth gravity
        Isp = 300  # specific impulse (s), placeholder value
        m0 = self.weight  # initial mass (kg)
        mf = m0 * 0.6  # final mass after fuel burn, placeholder ratio
        delta_v = Isp * g * math.log(m0 / mf)
        return delta_v

    def can_escape_planet(self, planet_name):
        planet_info = planets.get(planet_name.lower())
        if planet_info is None:
            print("Invalid Planet name.")
            return False
        planet_circumference, planet_mass = planet_info
        planet_radius = planet_circumference / (2 * math.pi)
        planet_escape_velocity = self.calculate_escape_velocity(planet_mass, planet_radius)
        rocket_final_velocity = self.calculate_final_velocity(planet_mass)

        if rocket_final_velocity > planet_escape_velocity:
            print(f"Rocket can escape {planet_name}.")
            return True
        else:
            print(f"Rocket cannot escape {planet_name}. Required thrust or fuel efficiency may need to be increased.")
            return False

rockets_set ={
    "PSLV": Rocket(44.4, 294500, 2.8, 7600000),  # Example thrust in Newtons
    "GSLV": Rocket(49.1, 418200, 3.7,8600000),
    "Falcon 9": Rocket(70, 549054, 3.7, 7607000),
    "Saturn V": Rocket(110.6, 2970000, 10.1, 35100000),
    "Delta IV Heavy": Rocket(72, 733000, 5, 9600000),
    }


# Planetary data (circumference in meters, mass in kg)
planets = {
    "mercury": (48.80 * 10 ** 5, 33.011 * 10 ** 23),
    "venus": (121.04 * 10 ** 5, 48.675 * 10 ** 24),
    "earth": (40.0664 * 10 ** 6, 59.8 * 10 ** 24),
    "mars": (67.92 * 10 ** 5, 64.171 * 10 ** 23),
    "jupiter": (1429.84 * 10 ** 5, 189.82 * 10 ** 27),
    "saturn": (1205.36 * 10 ** 5, 56.834 * 10 ** 26),
    "uranus": (507.24 * 10 ** 5, 86.81 * 10 ** 25),
    "neptune": (492.44 * 10 ** 5, 102.413 * 10 ** 24)
}

planets_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def main():
    print("some set of rockets examples\n")
    # Print the details of each rocket
    for rocket_name, rocket in rockets_set.items():
        print(f"{rocket_name}: {rocket}")

    print("\nThe planets in our solar system are:")
    for planet in planets_list:
        print(planet)

    while True:
        try:
            rocket_height = float(input("Enter rocket height (meters): "))
            rocket_weight = float(input("Enter rocket weight (kilograms):"))
            rocket_width = float(input("Enter rocket width (meters): "))
            planet_name = input("Enter planet name: ")
            rocket_thrust = float(input("Enter rocket thrust (Newtons): "))
            rocket = Rocket(rocket_height, rocket_weight, rocket_width, rocket_thrust)
            rocket.can_escape_planet(planet_name)
            return
        except Exception:
            print("Please provide valid values")

main()

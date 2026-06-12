# --- Initial variables representing physical properties ---


train_mass = 22680        # Mass of the GE train in kilograms
train_acceleration = 10  # Acceleration of the train in m/s²
train_distance = 100     # Distance traveled by the train in meters
bomb_mass = 1            # Mass of the bomb in kilograms


# Task 1: Function to convert Fahrenheit to Celsius

# Formula: (F - 32) * 5/9
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9  # Apply the Fahrenheit to Celsius conversion formula
  return c_temp                  # Return the result in Celsius


# Task 2: Test f_to_c with 100°F and store the result

f100_in_celsius = f_to_c(100)   # Convert 100 Fahrenheit to Celsius


# Task 3: Function to convert Celsius to Fahrenheit

# Formula: (C * 9/5) + 32
def c_to_f(c_temp):
  f_temp = ((c_temp * 9/5) + 32)  # Apply the Celsius to Fahrenheit conversion formula
  return f_temp                    # Return the result in Fahrenheit


# Task 4: Test c_to_f with 0°C and store the result

c0_in_fahrenheit = c_to_f(0)    # Convert 0 Celsius to Fahrenheit


# Task 5: Function to calculate force using Newton's second law (F = m * a)

def get_force(mass, acceleration):
  return mass * acceleration       # Multiply mass by acceleration to get force in Newtons


# Task 6: Calculate the force of the train using its mass and acceleration

train_force = get_force(train_mass, train_acceleration)  # Force = train_mass * train_acceleration


# Task 7: Print the force of the GE train in Newtons

print("The GE train supplies " + str(train_force) + " Newtons of force.")


# Task 8: Function to calculate energy using Einstein's mass-energy equivalence (E = mc²)

# c defaults to the speed of light in m/s (3 * 10^8)
def get_energy(mass, c=3*10**8):
  return mass * c**2               # Multiply mass by the square of the speed of light


# Task 9: Calculate the energy of the bomb using its mass and the default speed of light

bomb_energy = get_energy(bomb_mass)  # Energy = bomb_mass * c² (c defaults to 3*10^8 m/s)


# Task 10: Print the energy supplied by the bomb in Joules

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


# Task 11: Function to calculate work done (W = F * d), using get_force internally

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)  # First calculate force using mass and acceleration
  return force * distance                # Then multiply force by distance to get work in Joules


# Task 12: Calculate the work done by the train over its travel distance

train_work = get_work(train_mass, train_acceleration, train_distance)  # Work = force * distance


# Task 13: Print the work done by the GE train in Joules over the given distance

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

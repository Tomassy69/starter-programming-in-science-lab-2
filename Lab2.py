# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    pass  # Replace with your code


InitialHeight = float(input("Enter initial height: "))
Time = float(input("Enter time: "))
g = 9.8
HeightOfBall = InitialHeight - 1 / 2 * g * Time**2

print("Height of the ball at time", Time, "second =", HeightOfBall, "meters")


# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
speed=20
time_of_car=int(input("Enter time for car (in seconds):"))
distance=speed*time_of_car

print("The car will travel", distance, "meters in", time_of_car, "seconds.")

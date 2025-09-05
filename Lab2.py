# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
h0 = float(input("Enter initial height: "))
t = float(input("Enter time: "))
def calculate_height(t):
    return round(h0 - 1 / 2 * 9.8 * t**2, 1)
    # TODO: Implement this function
print("Height of the ball at", t, "second =", calculate_height(t), "meters")
# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
speed = float(20)
time = float(input("Enter time for car (in seconds):"))
def calculate_car_distance(time):
    return round(speed * time, 1)
    # TODO: Implement this function
print("The car will travel", calculate_car_distance(time), "meters in", time, "seconds.")

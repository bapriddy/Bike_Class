# Example of usage
#if __name__ == "__main__":
from bike import Bike 
    try:
        bike = Bike(5, 2, "hand brakes")  # Valid initialization
        print(f"Number of Gears: {bike.get_number_of_gears()}")
        print(f"Current Gear: {bike.get_current_gear()}")
        print(f"Number of Wheels: {bike.get_number_of_wheels()}")
        print(f"Brake Type: {bike.get_brake_type()}")

        bike.increase_gear()
        print(f"Current Gear after increasing: {bike.get_current_gear()}")

        bike.decrease_gear()
        print(f"Current Gear after decreasing: {bike.get_current_gear()}")

        bike.reset_gears()
        print(f"Current Gear after resetting: {bike.get_current_gear()}")
        # Attempting to set an invalid brake type
        bike.set_brake_type("electric brake")  # This will raise an error
        # Attempting to set an invalid number of gears
        bike.set_number_of_gears(20)  # This will raise an error
    except ValueError as e:
        print(e)  # Catch and print the error message

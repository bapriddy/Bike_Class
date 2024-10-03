class Bike:
    # Private properties
    __number_of_gears: int = 1
    __current_gear: int = 1
    __number_of_wheels: int = 2
    __brake_type: str = "hand brakes"

    ##################################
    # Instantiate a copy of this class
    def __init__(self, number_of_gears: int = 1, number_of_wheels: int = 2, brake_type: str = "hand brakes"):
        self.set_number_of_gears(number_of_gears)
        self.set_number_of_wheels(number_of_wheels)
        self.set_brake_type(brake_type)

    #########################################
    # Getter and setter for the number_of_gears property
    def get_number_of_gears(self) -> int:
        return self.__number_of_gears

    def set_number_of_gears(self, number_of_gears: int) -> None:
        if 1 <= number_of_gears <= 15:
            self.__number_of_gears = number_of_gears
        else:
            raise ValueError("Number of gears must be between 1 and 15.")

    ########################################
    # Getter and setter for the current_gear property
    def get_current_gear(self) -> int:
        return self.__current_gear

    def set_current_gear(self, current_gear: int) -> None:
        if 1 <= current_gear <= self.__number_of_gears:
            self.__current_gear = current_gear
        else:
            raise ValueError(f"Current gear must be between 1 and {self.__number_of_gears}.")

    #############################
    # Getter and setter for the number_of_wheels property
    def get_number_of_wheels(self) -> int:
        return self.__number_of_wheels

    def set_number_of_wheels(self, number_of_wheels: int) -> None:
        if number_of_wheels in [1, 2, 3, 4]:
            self.__number_of_wheels = number_of_wheels
        else:
            raise ValueError("Number of wheels must be 1, 2, 3, or 4.")

    ########################################
    # Getter and setter for the brake_type property
    def get_brake_type(self) -> str:
        return self.__brake_type

    def set_brake_type(self, brake_type: str) -> None:
        if brake_type in ["hand brakes", "foot brakes"]:
            self.__brake_type = brake_type
        else:
            raise ValueError("Brake type must be 'hand brakes' or 'foot brakes'.")

    # Reset current gear to 1
    def reset_gears(self) -> None:
        self.__current_gear = 1

    # Increase current gear
    def increase_gear(self) -> None:
        if self.__current_gear < self.__number_of_gears:
            self.__current_gear += 1
        else:
            raise ValueError("Cannot increase gear: already at maximum.")

    # Decrease current gear
    def decrease_gear(self) -> None:
        if self.__current_gear > 1:
            self.__current_gear -= 1
        else:
            raise ValueError("Cannot decrease gear: already at minimum.")


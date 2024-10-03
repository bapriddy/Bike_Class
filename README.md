# Bike Class in Python

## Description

This project implements a `Bike` class in Python, encapsulating various properties and methods related to a bike. The class allows you to manage the bike's gears, wheels, and brake type, providing a basic interface for interacting with a bike's functionality.

## Features

- Set and get the number of gears.
- Set and get the current gear (default is 1).
- Set and get the number of wheels (1 to 4).
- Set and get the brake type (either "hand brakes" or "foot brakes").
- Reset gears to 1.
- Increase or decrease the current gear, ensuring it stays within valid limits.

## Requirements

- Python 3.12.4 and up

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bapriddy/bike-class.git
   cd bike-class
from bike import Bike

# Usage

## Create a new bike instance
my_bike = Bike(number_gears=5, nummber_wheels=2, brake_type="hand brakes")

## Set current gear
my_bike.set_current_gear(3)

## Get current gear
print(my_bike.get_current_gear())  # Output: 3

## Increase gear
my_bike.increase_gear() # Output 4

## Decrease gear
my_bike.decrease_gear() # Output 3

## Reset gears
my_bike.reset_gears() # back to 1


#  Original Requirements 

## Create a Bike Class in python with the following properties
- Number of Gears
- Current Gear (should default to 1)
- Number of Wheels (1, 2, 3, or 4)
- Brake Type ("hand brakes" or "foot brakes")

## Then add the following methods
- Set & Get Number of Gears
- Set & Get Current Gear
- Set & Get Number of Wheels
- Set & Get Brake Type
- Reset Gears: Set gear back to 1
- Increase Gear: Increase Current Gear by 1, do not allow going over Number of Gears
- Decrease Gear: Decrease Current Gear by 1, do not allow going under 1

###############################################################################
# Exercise 1: Car Class with Encapsulation
###############################################################################

"""
Objective:
Create a Car class demonstrating encapsulation principles where the fuel level
is private and can only be accessed/modified through specific methods.

Key Concepts:
- Private attributes (using double underscore)
- Encapsulation
- Getter/Setter methods
- Input validation
- Basic calculations

Skills Practiced:
- Creating classes
- Implementing encapsulation
- Method definition
- Error handling
- Basic arithmetic operations

Requirements:
1. Create Car class with private fuel_level attribute
2. Implement add_fuel() method with validation
3. Implement drive() method with fuel consumption logic
4. Create getter method for fuel level
5. Test encapsulation by attempting direct attribute access
"""

###############################################################################
# Task Breakdown:
###############################################################################

"""
1. Class Creation:
   - Define Car class
   - Initialize private __fuel_level attribute
   
2. Method Implementation:
   - add_fuel(amount): Add fuel with positive value validation
   - drive(distance): Calculate fuel consumption (1L/10km)
   - get_fuel_level(): Return current fuel level
   
3. Testing:
   - Create car instance
   - Test all methods
   - Attempt direct access to __fuel_level
   
Example Usage:
    my_car = Car()
    my_car.add_fuel(50)    # Add 50L of fuel
    my_car.drive(100)      # Drive 100km (uses 10L)
    print(my_car.get_fuel_level())  # Should show 40L
"""

###############################################################################
# Extra Challenges:
###############################################################################

"""
Bonus Tasks:
1. Add fuel efficiency attribute (km/L)
2. Implement fuel capacity limit
3. Add warning when fuel is low (below 10%)
4. Track total distance driven
5. Calculate average fuel economy
"""

###############################################################################
# Sample Test Cases:
###############################################################################

"""
Test Scenarios:
1. Add negative fuel amount (should fail)
2. Drive without fuel (should fail)
3. Drive further than fuel allows (should fail)
4. Normal operations (should succeed)
5. Try accessing __fuel_level directly (should fail)
"""
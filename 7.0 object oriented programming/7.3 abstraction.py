
# Key Points About Abstraction

# Abstraction is about hiding complex implementation details and showing only the necessary features of an object. In Python, we achieve this using abstract classes and methods. Let me show you with a practical example:

# Hides Implementation Details: The user only interacts with the essential parts of the code, without knowing the internal workings.
# Achieved Using Abstract Classes: Abstract classes contain abstract methods that must be implemented in derived classes.
# Forces Subclasses to Implement Specific Methods: Ensures a consistent interface for all subclasse


# from abc import ABC, abstractmethod

# # Abstract class
# class Vehicle(ABC):
    
#     @abstractmethod
#     def start(self):
#         """Abstract method that must be implemented by subclasses"""
#         pass

#     @abstractmethod
#     def stop(self):
#         """Another abstract method"""
#         pass

# # Concrete class inheriting from Vehicle
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting...")

#     def stop(self):
#         print("Car is stopping...")

# # Concrete class inheriting from Vehicle
# class Bike(Vehicle):
#     def start(self):
#         print("Bike is starting...")

#     def stop(self):
#         print("Bike is stopping...")

# Trying to create an object of the abstract class will raise an error
# v = Vehicle()  # TypeError: Can't instantiate abstract class Vehicle

# Creating objects of concrete classes
# c = Car()
# c.start()  # Output: Car is starting...
# c.stop()   # Output: Car is stopping...

# b = Bike()
# b.start()  # Output: Bike is starting...
# b.stop()   # Output: Bike is stopping...





# example

# from abc import ABC, abstractmethod

# class Vehicle(ABC):  # ABC = Abstract Base Class
#     @abstractmethod
#     def start_engine(self):
#         pass
    
#     @abstractmethod
#     def stop_engine(self):
#         pass
    
#     def fuel_up(self):  # Regular method
#         print("Vehicle is fueling up")

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine starting with key turn")
        
#     def stop_engine(self):
#         print("Car engine stopped")

# class Motorcycle(Vehicle):
#     def start_engine(self):
#         print("Motorcycle engine starting with kick-start")
        
    # def stop_engine(self):
    #     print("Motorcycle engine stopped")



# example explaining 


# from abc import ABC, abstractmethod

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass

# class StripePayment(PaymentProcessor):
#     def process_payment(self, amount):
#         # Complex Stripe implementation hidden inside
#         self._connect_to_stripe()
#         self._verify_stripe_account()
#         self._handle_stripe_payment(amount)
#         self._verify_stripe_response()
#         print(f"Processed ${amount} through Stripe")
    
#     def _connect_to_stripe(self):
#         # Complex connection code here
#         pass
    
#     def _verify_stripe_account(self):
#         # Complex verification code here
#         pass
    
#     def _handle_stripe_payment(self, amount):
#         # Complex payment handling code
#         pass
    
#     def _verify_stripe_response(self):
#         # Complex response verification
#         pass

# class PayPalPayment(PaymentProcessor):
#     def process_payment(self, amount):
#         # Complex PayPal implementation hidden inside
#         self._init_paypal_client()
#         self._create_paypal_order(amount)
#         self._execute_paypal_payment()
#         print(f"Processed ${amount} through PayPal")
    
#     def _init_paypal_client(self):
#         # Complex initialization code
#         pass
    
#     def _create_paypal_order(self, amount):
#         # Complex order creation code
#         pass
    
#     def _execute_paypal_payment(self):
#         # Complex execution code
#         pass


# Now, when you use these payment processors, look how simple it is:
# pythonCopydef checkout(payment_processor, amount):
#     # The user of this code only needs to know about process_payment()
#     # They don't need to know anything about the complex steps inside
#     payment_processor.process_payment(amount)

# # Usage
# stripe = StripePayment()
# paypal = PayPalPayment()

# # Both work the same simple way, hiding their complexity
# checkout(stripe, 100)  # Processed $100 through Stripe
# checkout(paypal, 100)  # Processed $100 through P
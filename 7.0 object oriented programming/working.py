# complex code that start looking more complex, trying to do alots of things, trying to manage whole bunch of relationships

# code gets difficult to manage, becoming spaghetti

# this type of programming is know as procedural programming

# one procedure leads to another, computer is working from top to bottom
# one such earlier computer programs include-> cobol, fotran etc


# HOW CAN WE MANAGE COMPLEX CODE --> modularity, reusability

# OOP is all about splitting a large task into smaller pieces and each of this can be work by seperate teams and people  and can become reusable if we need same functionality in the future

# DIFFICULT TO CREATE A COMPLEX PROGRAM USING PROCEDURAL PROGRAMMING 


# called oop because its use to model real life objects

# in oop we have methods (what it does), and Attributes (What it has)


# attributes-> A fancy word for a fancy word for a variable, associated with a modeled object, 
# methods: a function that a particular object can do (its attach to an object)

# import turtle
# from turtle import Turtle, Screen

# # turtle.Turtle()
# my_turtle=Turtle()
# print(my_turtle)

# # # what can we do with an object, we can tab into its properties and methods
# my_turtle_screen=Screen()
# print(my_turtle_screen)
# # # print(my_turtle_screen.canvas)
# # my_turtle.shape("turtle")

# my_turtle_screen.exitonclick()

# import turtle

# def draw_rectangle(color, x, y, width, height):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.end_fill()

# def draw_triangle(color, x, y, size):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for _ in range(3):
#         turtle.forward(size)
#         turtle.left(120)
#     turtle.end_fill()

# def draw_circle(color, x, y, radius):
#     turtle.penup()
#     turtle.goto(x, y - radius)
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     turtle.circle(radius)
#     turtle.end_fill()

# def draw_house():
#     turtle.speed(3)
#     turtle.bgcolor("lightblue")
    
#     # Draw the ground
#     draw_rectangle("green", -300, -200, 600, 200)
    
#     # Draw the house base
#     draw_rectangle("blue", -100, -100, 200, 150)
    
#     # Draw the roof
#     draw_triangle("brown", -100, 50, 200)
    
#     # Draw the door
#     draw_rectangle("red", -30, -100, 60, 90)
    
#     # Draw windows
#     draw_rectangle("white", -80, -20, 40, 40)
#     draw_rectangle("white", 40, -20, 40, 40)
    
#     # Draw the sun
#     draw_circle("yellow", 200, 200, 50)
    
#     # Draw a tree trunk
#     draw_rectangle("brown", -250, -100, 30, 100)
    
#     # Draw tree leaves
#     draw_circle("darkgreen", -235, 20, 50)
#     draw_circle("darkgreen", -260, 40, 50)
#     draw_circle("darkgreen", -210, 40, 50)
    
#     # Hide turtle and display
#     turtle.hideturtle()
#     turtle.done()

# # # Call function to draw the house
# draw_house()





# using Prettytable class
# from prettytable import PrettyTable

# table_1=PrettyTable()
# table_2=PrettyTable()
# table_1.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table_1.add_column("Type", ["Electric", "Water", "Fire"])
# table_1.align="l"
# # table_1.dividers=1
# print(table_1)




# 3 ways of naming stuffs:
# - camelcasing: myNumber
# mynumberisnice=myNumberIsNice
# snake_Casing mynumber==my_number
# pascal casing: mynumber==MyNumber===>naming classes


# Blue print of the object
class User:
     def __init__(self,username, user_id, email, password):
         self.name=username
         self.id=user_id
         self.email=email
         self.password=password
        #  default attributes
         self.follower=0
     
     def print_email(self):
        return f"Your email is {self.email}"
     
     def print_username(self):
        return f"your email is {self.name}"
     def follows(self, user):
        self.follower+=1
        user.follower+=1
 
 
 
# creating instants of that object using our blue print 
user_1=User("Linus", "001", "linus@email.com", "qwerty")
user_2=User("Linus2", "002", "linus2@email.com", "qwerty2")
user_3=User("Linus3", "003", "linus3@email.com", "qwerty3")
# print_name= user_1.print_email()
# printing the information of user_1
# print(print_name)
# print(user_1.id)
# print(user_1.email)
# print(f"my followers are {user_1.follower}")



user_1.follows(user_2)
print(user_1.follower)
print(user_2.follower)
# print same info for user_2
# print(user_2.name)
# print(user_2.id)
# print(user_2.email)


# user_2=User()
# user_3=User()
# user_1.username="john"
# user_1.user_id="001"
# user_1.email="john@email.com"

# user_2.username="john2"
# user_2.user_id="002"
# user_2.email="john2@email.com"
 
 

# print(user_1.username)
# print(user_1.id)
# print(user_1.email)     






















# user_1=User()
# user_2=User()
# user_1.username="Henry"
# user_1.user_id="001"
# print(user_1.username)
# user_1.hello=say_hello()
# print(user_1.hello)
    
# class User:
#     def __init__(self, username, uid, password, email):
#         self.name=username
#         self.id=uid
#         self.password=password
#         self.email=email
#         self.followers=0
#         self.following=0
#         print("init constructor running")
#         # default attributes: we dont pass them into the constructor
#     # letter on please
#     def follower(self, user):
#         self.following+=1
#         user.followers+=1
     
# user_1=User("gita", "001", "1234", "@email.com")
# user_2=User("gita2", "002", "1235", "@gemail.com")
# # user_2=User()
# print(user_1.name)
# print(user_2.followers)
# print(user_1)

# print(user_2)

# # lets sau user_1 wamts to follow user 2
# user_1.follower(user_2)
# # user_2.follower(user_1)
# print(user_2.following)
# print(user_1.following)

# print(user_1.followers)

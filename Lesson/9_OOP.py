# # class Student : 
# #     name = "bayezid"
# # s1 = Student()
# # print (s1.name)


# # class Car:
# #     color = "blue"
# #     brand = "toyota"
# #     model = "prius"

# # def brandmodel(brand,model):
# #     return brand +" "+ model

# # car1 = Car()
# # print(car1.color)
# # print(car1.model)
# # print(car1.brand)

# # print(brandmodel("toyota","prius"))


# # Base Class (Parent)
# class Animal:
#     def __init__(self, name):
#         self.__name = name  # Private attribute (Encapsulation)

#     def speak(self):  # Abstract method (could be overridden)
#         raise NotImplementedError("Subclass must implement abstract method")
    
#     def get_name(self):  # Public method to access private attribute
#         return self.__name

# # Derived Class 1 (Child of Animal)
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Call parent constructor
#         self.breed = breed
    
#     # Polymorphism - Overriding the speak method
#     def speak(self):
#         return f"{self.get_name()} says Woof! (Breed: {self.breed})"

# # Derived Class 2 (Child of Animal)
# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
    
#     # Polymorphism - Overriding the speak method
#     def speak(self):
#         return f"{self.get_name()} says Meow! (Color: {self.color})"

# # Multiple Inheritance - Combining functionality from multiple classes
# class Robot:
#     def __init__(self, model):
#         self.model = model

#     def speak(self):
#         return f"I am {self.model}, beep boop!"  # Method overriding

# # Hybrid Class (Inherits from Animal and Robot)
# class RoboDog(Dog, Robot):
#     def __init__(self, name, breed, model):
#         Dog.__init__(self, name, breed)  # Init Dog part
#         Robot.__init__(self, model)  # Init Robot part

#     # Polymorphism - Overriding the speak method
#     def speak(self):
#         dog_speak = Dog.speak(self)  # Calls Dog's speak method
#         robot_speak = Robot.speak(self)  # Calls Robot's speak method
#         return f"{dog_speak} Also: {robot_speak}"

# # Encapsulation - Hidden method to be called only within class
# class Secretive:
#     def __hidden_method(self):
#         return "This is hidden from outside access!"
    
#     def public_method(self):
#         return f"Calling hidden method: {self.__hidden_method()}"

# # Class for demonstrating Static Method and Class Method
# class MathOperations:
#     PI = 3.1416  # Class variable

#     @staticmethod
#     def add(a, b):  # Static method - no self or cls required
#         return a + b
    
#     @classmethod
#     def circle_area(cls, radius):  # Class method - cls refers to the class
#         return cls.PI * radius * radius

# # Object Creation & Polymorphism demonstration
# if __name__ == "__main__":
#     dog = Dog("Buddy", "Golden Retriever")
#     cat = Cat("Whiskers", "White")
#     robo_dog = RoboDog("RoboBuddy", "Cyber Retriever", "X2000")

#     print(dog.speak())  # Buddy says Woof!
#     print(cat.speak())  # Whiskers says Meow!
#     print(robo_dog.speak())  # RoboDog + Robot hybrid response
    
#     # Encapsulation - Using public method to access hidden method
#     secretive = Secretive()
#     print(secretive.public_method())  # Access hidden method

#     # Static and Class Method demonstration
#     print(MathOperations.add(5, 7))  # Static method - 12
#     print(MathOperations.circle_area(10))  # Class method - Area of circle


# def sort_numbers(list):
#     list.sort()
#     return list

# numbers = [1, 5, 2, 9, 3, 22, 13]
# sorted_numbers = sort_numbers(numbers)

# print("Sorted list:",sorted_numbers)



# def convert(h):
#     if h < 0:
#         return "hours can't be negative"
#     elif h == 0:
#         return "0 hour means 0 "
#     else:
#         m = h * 60

#     return m

# h = float(input("Enter hours: "))
# m = convert(h)
# print(m,"minutes")




class Student:
    def __init__(self, name, roll_no):
        self.name = name        
        self.roll_no = roll_no  

    def display(self):
        print(" Name:", self.name ,"\n", "Roll No:", self.roll_no)

student1 = Student("John", 2)
student1.display()

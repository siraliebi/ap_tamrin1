from abc import ABC,abstractmethod

class Animal(ABC):

    def __init__(self, name:None,age:None, gender:None, weight:None, height:None, **kwargs):
        
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        
    def move(self):
        pass
    
    def eat(self):
        pass
        
    def breath(self):
        pass
        
    def make_sound(self):
        pass
        
    def drink(self):
        pass

class Zoo(Animal):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Birds(Animal):
    
    def __init__(self, age, gender, wings_count, feather_count):
        self.age = age
        self.gender = gender
        self.wings_count = wings_count
        self.feather_count = feather_count
        
    def move(self):
        print('flies')
        
    def eat(self):
        print('eats')
        
    def make_sound(self):
        print('speaks')
    
    def mate(self):
        print('yes or no')
    
    def is_wild(self):
        print('yes or no')

class Mammals(Animal):
    
    def __init__(self):
        
    def give_birth(self):
        print('give birth')    
    
    def (self):
        print('breast feed')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('') 
        
class Reptiles(Animal):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('') 
        
class Amphibians(Animal):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Fish(Animal):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Eagle(Birds):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Pigeon(Birds):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Human(Mammals):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Snake(Reptiles):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Turtle(Reptiles):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
    
class Frog(Amphibians):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Shark(Fish):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
        
class Wale(Fish):
    
    def __init__(self, ):
        
    def (self):
        print('')    
    
    def (self):
        print('')
        
    def (self):
        print('') 
        
    def (self):
        print('') 
    
    def (self):
        print('')
    
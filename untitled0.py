from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, **kwargs):
        self._name = name
        self._age = age
        self._other_attributes = kwargs

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print(f"{self._name} is eating.")

    def sleep(self):
        print(f"{self._name} is sleeping.")

    def drink(self):
        print(f"{self._name} is drinking.")

    def move(self):
        print(f"{self._name} is moving.")

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def other_attributes(self):
        return self._other_attributes

class Bird(Animal):
    def __init__(self, name, age, wing_size, **kwargs):
        super().__init__(name, age,**kwargs)
        self._wing_size = wing_size

    def make_sound(self):
        print(f"{self.name} is making sound.")

    def fly(self):
        print(f"{self.name} is flying.")

    def rest(self):
        print(f"{self.name} is resting.")

    def breath(self):
        print(f"{self.name} is breathing.")

class Mammal(Animal):
    def __init__(self,name ,age,hair_color,**kwargs ):
        super().__init__(name ,age,**kwargs )
        self._hair_color=hair_color

    def make_sound(self):
        print(f"{self.name} makes a mammal sound.")

    def run(self):
        print(f"{self.name} is running.")

    def walk(self):
        print(f"{self.name} is walking.")

    def groom(self):
        print(f"{self.name} is grooming.")

class Reptile(Animal):
    def __init__(self,name ,age,skin_color,**kwargs ):
        super().__init__(name ,age,**kwargs )
        self._skin_color=skin_color

    def make_sound(self):
        print(f"{self.name} is making sound.")

    def crawl(self):
        print(f"{self.name} is crawling.")

    def rest(self):
        print(f"{self.name} is relaxing.")

    def shed_skin(self):
        print(f"{self.name} is shedding the skin.")

class Amphibian(Animal):
    def __init__(self,name ,age ,skin_color ,**kwargs ):
        super().__init__(name ,age ,**kwargs)
        self._skin_color=skin_color

    def make_sound(self):
        print(f"{self.name} is ghoor ghooring.")

    def swim(self):
        print(f"{self.name} is swimming.")

    def jump(self):
        print(f"{self.name} is jumping.")

    def breath(self):
        print(f"{self.name} is breathing.")

class Fish(Animal):
    def __init__(self,name ,age,breed,**kwargs ):
        super().__init__(name ,age,**kwargs )
        self._breed= breed

    def make_sound(self):
        print(f"{self.name} makes a fish sound.")

    def swim(self):
        print(f"{self.name} is swimming.")
        
class Eagle(Birds):
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
    def __init__(self, **kwargs):
        super().__init__()

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
        
class Zoo():
    
    def __init__(self, **kwargs):
        super().__init__()

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
    
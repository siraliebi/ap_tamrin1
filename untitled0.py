#For Abstraction
from abc import ABC, abstractmethod

class Animal(ABC):
    #encapsulation
    def __init__(self, name, age):
        self.name = name
        self._age = age
        
    #Abstraction
    @abstractmethod
    #polymorphism
    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def drink(self):
        print(f"{self.name} is drinking.")

    def move(self):
        print(f"{self.name} is moving.")

    #these two methods access to encapsulation private and protected attributes 
    def name(self):
        return self.name

    
    def age(self):
        return self._age

#Aggregation  
class Feather:
    def __init__(self, color):
        self.color = color

class Bird(Animal):
    def __init__(self, name, age, wing_size, feather,color, **kwargs):
        super().__init__(name, age,**kwargs)
        #encapsulation
        self._wing_size = wing_size
        #Aggregation
        self.feather = feather
        self.color = color
    #polymorphism
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
        #encapsulation
        self._hair_color=hair_color
    #polymorphism
    def make_sound(self):
        print(f"{self.name} makes a mammal sound.")

    def run(self):
        print(f"{self.name} is running.")

    def walk(self):
        print(f"{self.name} is walking.")

    def groom(self):
        print(f"{self.name} is grooooming.")

class Reptile(Animal):
    def __init__(self,name ,age,scale_color,**kwargs ):
        super().__init__(name ,age,**kwargs )
        #encapsulation
        self._scale_color=scale_color
       
    #polymorphism
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
        #encapsulation
        self._skin_color=skin_color
    #polymorphism
    def make_sound(self):
        print(f"{self.name} is making amphibian sound.")

    def swim(self):
        print(f"{self.name} is swimming.")

    def jump(self):
        print(f"{self.name} is jumping.")

    def breath(self):
        print(f"{self.name} is breathing.")

class Fish(Animal):
    def __init__(self,name ,age,breed,power,**kwargs ):
        super().__init__(name ,age,**kwargs )
        #encapsulation
        self._breed= breed
        self.power = power
    #polymorphism
    def make_sound(self):
        print(f"{self.name} makes a fish sound.")

    def swim(self):
        print(f"{self.name} is swimming.")
        
class Eagle(Bird):
    
    def __init__(self, name, age, wing_size, color,furcount, **kwargs):
        super().__init__(name ,age,wing_size,**kwargs )
        self.color=color
        self.__furcount = furcount

    def furs(self):
        return (f'{self.__furcount} is your furcount' )
    
    def move(self):
        print(f"{self.name} is flying.")    
    
    def eat(self):
        print(f"{self.name} is eating warms.")
        
class Pigeon(Bird):
    
    def __init__(self, name, age, wing_size, color, **kwargs):
        super().__init__(name ,age,wing_size,**kwargs )
        self.color=color

    def move(self):
        print(f"{self.name} is flying slowly.")    
    
    def eat(self):
        print(f"{self.name} is eating.")

#Composition       
class Heart:

    def __init__(self, beat):
        self.beat = beat

    def beating (self):
        print(f"heart is beating {self.beat} beats per minute")

class Human(Mammal):

    def __init__(self, name, age, hair_color, nationality, **kwargs):
        super().__init__(name, age, hair_color, **kwargs)
        self.nationality = nationality
        #Composition
        self.heart = Heart(60)

    def make_sound(self):
        print(f"{self.name} is speaking.")
        
    def drink(self):
        print(f"{self.name} is drinking.")
        
class Cat(Mammal):

    def __init__(self,name ,age ,hair_color ,breed ,**kwargs ):
        super().__init__(name ,age ,hair_color ,**kwargs)
        self.breed=breed

    def make_sound(self):
        print(f"{self.name} is meooowing.")
        
    def drink(self):
        print(f"{self.name} is drinking milk.")

class Lizard(Reptile):

    def __init__(self,name ,age,scale_color,length,**kwargs ):
        super().__init__(name ,age,scale_color,**kwargs )
        self.length=length
    
    def make_sound(self):
        print(f"{self.name} is silent.")

class Snake(Reptile):

    def __init__(self,name ,age,scale_color,length,**kwargs ):
        super().__init__(name ,age,scale_color,**kwargs )
        self.length=length
    
    def make_sound(self):
        print(f"{self.name} is hissing.")

    def hunt(self):
        print(f"{self.name} is hunting small animals.")

class Frog(Amphibian):

    def __init__(self,name ,age,skin_color,jump_heigth,**kwargs ):
        super().__init__(name ,age,skin_color,**kwargs )
        self.jump_heigth=jump_heigth
    
    def make_sound(self):
        print(f"{self.name} is ghooor ghooring.")

class Shark(Fish):
    
    def __init__(self,name, age, skin_color,breed, power, **kwargs):
        super().__init__(name, age, skin_color,breed,power, **kwargs)
        self.skin_color = skin_color

    def hunt(self):
        print(f"{self.name} is hunting animals.")

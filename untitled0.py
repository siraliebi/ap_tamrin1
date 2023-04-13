class Animal:

    def __init__(self, age, gender, weight, height, color):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.color = color
        
    def move(self):
        print('moving')
    
    def eat(self):
        print('eating')
        
    def breath(self):
        print('breathing')
        
    def speak(self):
        print('speaking')
        
    def drink(self):
        print('drinking')

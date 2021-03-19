class Player():
    DefaultAge = 22 #Class attribute 
    def __init__(self,name,age=20):
        self.name = name
        self.age = age
    def run(self):
        print('Run ',self.name)
   
    
class Wizard(Player):
    def __init__(self,age=20):
         super().__init__(age)
    def attack(self,power):
        print(f"Attcke with : {power}")

class MinWizard(Wizard):
    pass

class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
    def __str__(self):
        return (f"Toy with {self.color} Color and {self.age} Age")
    


toy1 = Toy('red', 12)
print(str(toy1))

print(str())


player01 = Player('Yasser',44)
player02 = Wizard('Amine')
player03 = MinWizard('Kamel')

player01.run()
print(player01.age)
#player03.attack(12)


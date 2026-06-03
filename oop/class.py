class Person: 
    def __init__(self, name):
        self.name = name 
        
    def info(self):
        print(f"your name {self.name}")
    
    
p1 = Person("Fahad")

p1.info()

p2 = Person("")
p2.name = "Mulon"
p2.info()

del p1.name

p1.info()
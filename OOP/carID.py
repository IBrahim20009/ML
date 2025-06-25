class Car :
    
    def __init__(self,make,year,model,color):
        self.make = make
        self.year = year
        self.model = model
        self.color = color 

    def driving(self):
        print(f"This {self.model} is driving.")
    def stop(self):
        print(f"This {self.model} is stopped.")
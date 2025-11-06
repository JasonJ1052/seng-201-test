import math

class patientrecord: 
    def __init__(self, name, age, height, weight):
        if age<0 or height<0 or weight<0:
            raise ValueError("age, height, and weight must all be > 0")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


    

    def printInfo(self, units):
        if units=='metric':
            print(f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg")
        elif units == 'imperial':
            print(f"Name: {self.name}, Age: {self.age}, Height: {round(self.height / 30.48, 1)}ft, Weight: {round(self.weight * 2.205,1)}lbs")
        else:
            print("I don't understand that unit.")
    



if __name__ == "__main__":
    bob = patientrecord("Bob", 50, 175, 85)
    claire = patientrecord("Claire", 21, 160, 54)
    print(bob.printInfo('metric'))
    print(claire.printInfo('imperial'))

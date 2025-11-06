import math

class PatientRecord:  # class names are always PascalCase
# One blank line between class and method definitions
    def __init__(self, name: str, age: int, height: int, weight: float):  # function + var names are always lowercase with underscores _
        """
        The class constructor. Raise an exception if age, height, or weight is <= 0
        :param name: person's name as a full string
        :param age: person's age in years
        :param height: in centimeters
        :param weight: in kilograms as a decimal
        """
        # don't do this
        # self.name, self.age, self.weight, self.height = name, age, weight, height
        # one variable assignment per line
        # If you need a multie-line comment in your Python code
        # You do it like this. Don't use """ for commenting other than for docstrings
        if age <0 or height < 0 or weight < 0:
            raise ValueError("age, height, and weight must all be > 0")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    # one blank link between methods
    def compute_risk(self) -> float:
        """
        compute the health risk index as
        HRI = 100 / (1 + e^(-z))
        z = −5 + 0.05(age−40) + 0.10(BMI-22) + 0.006(BMI−22)^2
        :return: the health risk index. Values will be 0 or above
        """
        bmi = self.compute_bmi()
        z = -5 + 0.05 * (self.age - 40) + 0.1*(bmi - 22) + 0.006*(bmi-22)**2
        return 100 / (1 + math.e**(-z))
    
    def compute_bmi(self) -> float:
        """
        compute their BMI as BMI = height / weight^2
        """
        return self.weight / (self.height / 100)**2
    
    def print_info(self, units: str) -> None:
        if units == 'metric':
            result = f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm, Weight: {self.weight}kg"
            result += f"\nBMI: {round(self.compute_bmi(), 1)}"
            result += f"\nHealth Risk Index: {round(self.compute_risk(), 1)}"
        elif units == 'imperial':
            result = f"Name: {self.name}, Age: {self.age}, Height: {round(self.height / 30.48, 1)}ft, Weight: {round(self.weight * 2.205,1)}lbs"
            result += f"\nBMI: {round(self.compute_bmi(), 1)}"
            result += f"\nHealth Risk Index: {round(self.compute_risk(), 1)}"
        else:
            result = "I don't understand that unit."
        print(result)
    

# Two blank lines after a class.    

if __name__ == "__main__":
    bob = PatientRecord("Bob", 50, 175, 85)
    claire = PatientRecord("Claire", 21, 160, 54)

    print(bob.print_scores(units='metric'))
    print(claire.print_scores(units='imperial'))

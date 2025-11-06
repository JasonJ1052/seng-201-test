class Patient:
    """Represents a patient in the hospital."""

    def __init__(self, name, age, weight, height):
        """Constructor for the Patient class

        Args:
            name (_str_): first and last name
            age (_int_): age in years
            weight (_int_): weight in pounds
            height (_int_): height in inches
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def compute_risk(self):
        """Compute the patient's risk of heart attack as: sqrt(age) - (height/weight)

        Returns:
            _float_: The patient's heart attack risk factor.
        """

        return self.age**0.5 - (self.height / self.weight)
    

if __name__ == "__main__":
    bob = Patient("Bob Bobberton", 54, 200, 65)
    claire = Patient("Claire DeLune", 21, 115, 65)

    print(bob.compute_risk())
    print(claire.compute_risk())

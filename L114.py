#The author's names are Colleen and Rylee
class Fabric:
    def __init__(self, countryOfOrigin, color):
        self.countryOfOrigin = countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "("+ self.color + ")"

f1 = Fabric("America", "red")

print(f1)


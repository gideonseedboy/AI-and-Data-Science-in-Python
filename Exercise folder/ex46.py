# Functions with Dictionaries


car = {"brand":"Toyota","model":"Yaris","color":"Wine","year":2017, "made":"Cameroon", "used":"Private"}


car["CC"] = 1500
car["Chasis"] = "010035330001"
car["Condition"] = "Usable"

len(car)

#pop function => It removes an specific value from the dictionaary

car.pop("brand") #It has removed the Key and the avalue
car.pop("made")
 # Remembeer that the List uses the index to remove the element

#item function
car.popitem() #This,  without any futhere parameters it removes the laast item in the dictionary

print(len(car))
print(car)
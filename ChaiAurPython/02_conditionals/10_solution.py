'''Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).'''

species=input("Enter Species type :")
age=int(input("Enter Species Age: "))
if species=="Dog":
    if age< 2:
        pet_food="Puppy food"
    else:pet_food="Senior Dog Food"
if species=="Cat":
    if age>5:
        pet_food="Senior cat food"
    else:pet_food="citty food"

print(species,pet_food)
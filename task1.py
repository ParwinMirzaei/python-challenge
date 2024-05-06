class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"Woof! My name is {self.name}.")
#Instantiate two dogs
dog1 = Dog("Max", 4)
dog2 = Dog("Daisy", 3)
# Store them in a list called dog_pack
dog_pack = [dog1, dog2]
print("Barking:")
for dog in dog_pack:
    dog.bark()
#the average age of all dogs in the list
total_age = 0
for dog in dog_pack:
    total_age += dog.age
average_age = total_age / len(dog_pack)
print(f"Average age of all dogs: {average_age}")
# Loops
doctor =1 

while doctor<=10:
    print(f"Examinate Doctor {doctor}!")
    doctor +=1

# For Loop: Strings
for char in "Python":
    print(char)

# For Loop: Ranges
# 1
for number in range(77,100):
    print(number)

# 2
for number in range(77,100,2):
    print(number)

# For Loop: Lists
products=["Apps","Website","PosSystem","Marketing"]

for product in products:
    print("Our products:",product)

# For Loop: Dictionaries
legs = {"humans":2, "eagle":2, "lion":4}

for (animal,number) in legs.items(): 
    print("{} has {} legs".format(animal,number))

    

# Variables = string(str = characters) , integer(int = whole number) , float(float = To use decimal) , boolean( = True or False)

# Example

name = str(input("Whats your name?:"))

print(f"Hello {name} .Thats a cool name!")

food = str(input("Which food would you like to order?:"))

print(f"So your choice is {food} huh? You have a good taste!")

print(f"The price of a {food} is 150 Taka")

location = str(input("Please give your location here: "))

print(f"{name} , be sure that your location is {location}")

amount = int(input(f"Now please enter the amount of {food} you want: "))

print("Cool, it will be:Taka ",150*amount)
num_spaces = 0

while True:
    try:
        size = int(input("Enter an integer: "))
        if size % 2 == 0:
            raise ValueError("Error occurred: You entered an even number.")
        else:
            break
    except ValueError as e:
        print("invalid data type or number not odd")
    
num_asterisks = size 
for i in range(size):
    spaces = " " * num_spaces
    asterisks = "*" * num_asterisks
    print(f"{spaces}{asterisks}{spaces}")
    
    if i < size // 1:
        num_spaces += 1
        num_asterisks -= 2
   
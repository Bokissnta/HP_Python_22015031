while True:
    try:
        num = int(input("Type a number: "))
    except ValueError:
        print("Only integer character is allowed, try again")
        continue
    break

for b in range(num):
    print("#"*(b+1))
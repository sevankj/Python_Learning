try:
    count = int(raw_input("give me a number: "))
except ValueError:
    print("Thats not a numnber !")
else:
    print("Hi " * count)

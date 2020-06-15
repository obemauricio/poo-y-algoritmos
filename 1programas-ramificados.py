name1 = input("What's your name?: ")
name2 = input("what's your friend's name?: ")
age1 = int(input("What´s your age?: "))
age2 = int(input("What's your friend's age?: "))
if age1 > age2: 
    print(f"you're more old than {name2}")
elif age1 < age2: 
    print(f"{name2} is more old than {name1}")
else:
    print(f"{name2} is the same age than {name1}")    
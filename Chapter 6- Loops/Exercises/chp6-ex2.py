while True:
    age = input("Enter your age: ")

    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket will cost 10AED")
    else:
        print("Your ticket will cost 15AED")
mydict = {}

matrix_size = int(input("Matrix size: "))

for i in range(matrix_size):
    item = input(f"Shopping item{i+1}: ")
    mydict[i] = item

print(f"\nYou have {len(mydict)} items in the cart")

while True:
    choice = input("\nWhat would you like to do [C]hange items [R]emove [D]isplay S[earch] ? (* to exit) ").strip().lower()

    if choice == "*":
        print("Bye")
        break

    elif choice == "d":
        print("\nDisplaying Values")
        print("Key   Value")
        for key, value in mydict.items():
            print(f"{key}    {value}")

    elif choice == "s":
        search_item = input("Enter item to search: ").strip()
        found = False

        for key, value in mydict.items():
            if value.lower() == search_item.lower():
                print(f"Found {value} item")
                found = True
                break
        if not found:
            print("I'm sorry, not in the cart")

    elif choice == "r":
        key_input = input("Enter key to search: ")
        
        if key_input.isdigit():
            key_input = int(key_input)
            value = mydict.get(key_input)
            if value is not None:
                del mydict[key_input]
                print(f"The key {key_input} with value {value} has been deleted")
            else:
                print("Key not found")
        else:
            print("Invalid key, please enter a number.")

    elif choice == "c":
        key_input = input("Enter key to search: ")
        if key_input.isdigit():
            key_input = int(key_input)
            value = mydict.get(key_input)
            if value is not None:
                print(f"Found {value} item")
                new_value = input("Enter value: ")
                mydict[key_input] = new_value
                print(f"Key {key_input} is now updated to {new_value}")
            else:
                print("I'm sorry, not in the cart")
        else:
            print("Invalid key, please enter a number.")

    else:
        print("Invalid choice! Please choose C, R, D, S, or *")

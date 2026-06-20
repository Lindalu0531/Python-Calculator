import os

def main():
    def clear():
        input("\nEnter Return to clear the screen")
        os.system("cls" if os.name == "nt" else "clear" )

    def addition(x, y):
        return x + y

    def substraction(x, y):
        return x - y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        if x == 0 or y == 0:
            return "Cant Divide!"
        return x / y

    def exponation(x, y):
        return x ** y
    print("Welcome To Calculator")

    print("\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Quit")
    while True:
        try:
            choice = int(input("Enter the id to performe and action eg: 1, 2, 3, 4, 5, 6: "))
        except ValueError:
            print("Enter valid number")
            continue
        if choice == 6:
            print("Bye, :D")
            break
        elif choice > 6:
            print("Invalid option")
            continue
        try:
            enter = float(input("Enter number one: "))
            enter1 = float(input("Enter number two: "))
        except ValueError:
            print("Enter a valid number")
            continue

        try:
            if choice == 1:
                print(addition(enter, enter1))
            elif choice == 2:
                print(subtraction(enter, enter1))
            elif choice == 3:
                print(multiplication(enter, enter1))
            elif choice == 4:
                print(division(enter, enter1))
            elif choice == 5:
                print(exponation(enter, enter1))
            else:
                print("Invalid Choice!")
            clear()
            print("\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Quit")
        except ValueError:
            print("Please enter a valid number")
            break


if __name__ == "__main__":
    main()
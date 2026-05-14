import os

def main():
    def clear():
        input("\nEnter Return to clear the screen")
        os.system("cls" if os.name == "nt" else "clear" )

    def addition(x, y):
        return x + y
        clear()

    def substraction(x, y):
        return x - y

    def multiplication(x, y):
        return x * y

    def division(x, y):
        if x == 0 or y == 0:
            return "Cant Divide!"
        return x / y

    print("Welcome To Calculator")

    print("\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Quit")
    while True:
        
        choice = int(input("Enter the id to performe and action eg: 1, 2, 3, 4, 5: "))
        if choice ==5:
            print("Bye, :D")
            break

        enter = float(input("Enter number one: "))
        enter1 = float(input("Enter number two: "))

        if choice == 1:
            print(addition(enter, enter1))
        elif choice == 2:
            print(substraction(enter, enter1))
        elif choice == 3:
            print(multiplication(enter, enter1))
        elif choice == 4:
            print(division(enter, enter1))
        else:
            print("Invalid Choice!")
        clear()

if __name__ == "__main__":
    main()
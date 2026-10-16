stack = [0] * 5
top = -1
size = 5

while True:
    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            if top == size - 1:
                print("Stack is full")
            else:
                value = int(input("Enter value: "))
                top += 1
                stack[top] = value
                print("Element pushed")

        case 2:
            if top == -1:
                print("Stack is empty")
            else:
                print("Popped element:", stack[top])
                top -= 1

        case 3:
            if top == -1:
                print("Stack is empty")
            else:
                print("Top element:", stack[top])

        case 4:
            if top == -1:
                print("Stack is empty")
            else:
                print("Stack elements:", end=" ")
                for i in range(top, -1, -1):
                    print(stack[i], end=" ")
                print()

        case 5:
            print("Program closed")
            break

        case _:
            print("Invalid choice")

queue = [0] * 5
front = 0
rear = -1
size = 5

while True:
    print("\n===== QUEUE MENU =====")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            if rear == size - 1:
                print("Queue is full")
            else:
                value = int(input("Enter value: "))
                rear += 1
                queue[rear] = value
                print("Element inserted")

        case 2:
            if front > rear:
                print("Queue is empty")
            else:
                print("Deleted element:", queue[front])
                front += 1

        case 3:
            if front > rear:
                print("Queue is empty")
            else:
                print("Queue elements:", end=" ")
                for i in range(front, rear + 1):
                    print(queue[i], end=" ")
                print()

        case 4:
            print("Program closed")
            break

        case _:
            print("Invalid choice")

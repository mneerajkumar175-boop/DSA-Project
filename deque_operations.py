dq = [0] * 5
start = -1
end = -1
size = 5

while True:
    print("\n===== DEQUE MENU =====")
    print("1. Insert from front")
    print("2. Insert from rear")
    print("3. Delete from front")
    print("4. Delete from rear")
    print("5. Display deque")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            if end == size - 1:
                print("Deque is full")
            else:
                item = int(input("Enter element: "))

                if start == -1:
                    start = end = 0
                else:
                    k = end
                    while k >= start:
                        dq[k + 1] = dq[k]
                        k -= 1
                    end += 1

                dq[start] = item
                print("Inserted at front")

        case 2:
            if end >= size - 1:
                print("Deque is full")
            else:
                item = int(input("Enter element: "))

                if start == -1:
                    start = 0
                    end = 0
                else:
                    end += 1

                dq[end] = item
                print("Inserted at rear")

        case 3:
            if start == -1:
                print("Deque is empty")
            else:
                print("Deleted item:", dq[start])

                if start == end:
                    start = end = -1
                else:
                    start = start + 1

        case 4:
            if start == -1:
                print("Deque is empty")
            else:
                print("Deleted item:", dq[end])

                if start == end:
                    start = end = -1
                else:
                    end = end - 1

        case 5:
            if start == -1:
                print("Nothing to display")
            else:
                print("Deque elements:", end=" ")
                for k in range(start, end + 1):
                    print(dq[k], end=" ")
                print()

        case 6:
            print("Program closed")
            break

        case _:
            print("Invalid choice")

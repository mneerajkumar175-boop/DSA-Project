arr = [0] * 100
n = int(input("Enter number of elements: "))

for i in range(n):
    arr[i] = int(input("Enter value: "))

while True:
    print("\n===== ARRAY MENU =====")
    print("1. Insert element")
    print("2. Delete element")
    print("3. Show array")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            pos = int(input("Enter position: "))
            num = int(input("Enter element to insert: "))

            if pos > 0 and pos <= n + 1 and n < 100:
                j = n
                while j >= pos:
                    arr[j] = arr[j - 1]
                    j -= 1

                arr[pos - 1] = num
                n += 1
                print("Insertion successful")
            else:
                print("Invalid position or array is full")

        case 2:
            pos = int(input("Enter position to delete: "))

            if pos >= 1 and pos <= n:
                j = pos - 1
                while j < n - 1:
                    arr[j] = arr[j + 1]
                    j += 1

                n -= 1
                print("Deletion successful")
            else:
                print("Invalid position")

        case 3:
            if n == 0:
                print("Array is empty")
            else:
                print("Array elements:", end=" ")
                for i in range(n):
                    print(arr[i], end=" ")
                print()

        case 4:
            print("Program terminated")
            break

        case _:
            print("Wrong choice, try again")

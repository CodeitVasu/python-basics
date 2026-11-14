students = {}

while True:
    print("\n1. Add student  2. Update grade  3. Print all grades  4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")
        if name in students:
            print(name, "already exists. Use update instead.")
        else:
            students[name] = input("Grade: ")
            print("Added.")
    elif choice == "2":
        name = input("Student name: ")
        if name in students:
            students[name] = input("New grade: ")
            print("Updated.")
        else:
            print(name, "not found.")
    elif choice == "3":
        if len(students) == 0:
            print("No students yet.")
        else:
            for name, grade in students.items():
                print(name + ": " + grade)
    elif choice == "4":
        break
    else:
        print("Invalid option.")

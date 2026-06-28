students = []

def add_student():
    name = input("Student name: ")
    level = input("English level: ")

    student = {
        "name": name,
        "level": level
    }

    students.append(student)
    print("Student added successfully!")


def list_students():
    if not students:
        print("No students registered.")
        return

    print("\nStudents:")
    for student in students:
        print(f"Name: {student['name']} | Level: {student['level']}")


while True:
    print("\n=== ENGLISH CLASS MANAGER ===")
    print("1 - Add student")
    print("2 - List students")
    print("0 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_student()
    elif option == "2":
        list_students()
    elif option == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

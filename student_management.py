
students = {}

def student_add(student_id, name, grades):
    students[student_id] = {
        "naam": name,
        "grades": grades,
        "gpa": sum(grades) / len(grades)
    }
    print(f"{name} Added!")

def student_view(student_id):
    if student_id in students:
        s = students[student_id]
        print(f"\n--- {s['name']} ---")
        print(f"GPA: {s['gpa']:.2f}")
        print(f"Grades: {s['grades']}")
    else:
        print("Student not  Found!")

def honor_roll():
    print("\n Honor Roll (GPA >= 3.5):")
    for sid, s in students.items():
        if s["gpa"] >= 3.5:
            print(f"  {s['name']} — GPA: {s['gpa']:.2f}")

def all_students():
    print("\n Sab Students:")
    for sid, s in students.items():
        print(f"  {sid}: {s['naam']} | GPA: {s['gpa']:.2f}")

# Sample data
student_add("S001", "Sara", [90, 85, 92, 88])
student_add("S002", "Ali", [70, 65, 72, 68])
student_add("S003", "Fatima", [95, 98, 92, 96])

# Menu
while True:
    print("\n Student Management System ")
    print("1. Student Add")
    print("2. Student See")
    print("3. Honor Roll")
    print("4. Check All")
    print("5. Exit")

    choice = input("Option: ")

    if choice == "1":
        sid = input("ID: ")
        name = input("Name: ")
        g = input("Grades (comma separated): ")
        grades = [int(x) for x in g.split(",")]
        student_add(sid, name, grades)
    elif choice == "2":
        sid = input("Student ID: ")
        student_view(sid)
    elif choice == "3":
        honor_roll()
    elif choice == "4":
        all_students()
    elif choice == "5":
        print("Bye!")
        break
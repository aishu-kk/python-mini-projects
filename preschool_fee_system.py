
class PreschoolFeeSystem:

    def __init__(self):
        self.students = []

    def add_student(self):

        name = input("Enter student name: ")
        school_fee = float(input("Enter school fee: "))
        transport_fee = float(input("Enter transport fee: "))
        tuition_fee = float(input("Enter tuition fee: "))

        student = {
            "name": name,
            "school_fee": school_fee,
            "transport_fee": transport_fee,
            "tuition_fee": tuition_fee,
            "paid": 0
        }

        self.students.append(student)

        print("Student added successfully!")

    def show_students(self):

        if not self.students:
            print("No students found.")
            return

        print("\n--- Student Details ---")

        for s in self.students:

            total = s["school_fee"] + s["transport_fee"] + s["tuition_fee"]
            pending = total - s["paid"]

            print("\nName:", s["name"])
            print("School Fee:", s["school_fee"])
            print("Transport Fee:", s["transport_fee"])
            print("Tuition Fee:", s["tuition_fee"])
            print("Total Fee:", total)
            print("Paid:", s["paid"])
            print("Pending:", pending)

    def pay_fees(self):

        name = input("Enter student name: ")

        for s in self.students:

            if s["name"] == name:

                amount = float(input("Enter payment amount: "))
                s["paid"] += amount

                print("Payment updated successfully!")
                return

        print("Student not found.")


# ---------- MENU ----------
system = PreschoolFeeSystem()

running = True

while running:

    print("\n--- Preschool Fee Management ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Pay Fees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.show_students()

    elif choice == "3":
        system.pay_fees()

    elif choice == "4":
        print("Exiting program...")
        running = False

    else:
        print("Invalid choice!")

class FeeTracker:

    def __init__(self):
        self.students = []
    
    def add_student(self):
        name=input("Enter student name: ")
        school_fee=float(input("Enter school fee: "))
        transport_fee=float(input("Enter transport fee: "))

        student={
            "name": name,
            "school_fee": school_fee,
            "transport_fee": transport_fee,
            "paid": 0
         }

        self.students.append(student)
        print("Student added successfully!")

    def show_students(self):

        if not self.students:
            print("No students found.")
            return
        
        print("\n---Students Details---")

        for s in self.students:
            total=s["school_fee"]+s["transport_fee"]
            pending=total-s["paid"]

            print(f"\nName: {s['name']}")
            print(f"School Fee: {s['school_fee']}")
            print(f"Transport Fee: {s['transport_fee']}")
            print(f"Total Fee: {total}")
            print(f"Paid: {s['paid']}")
            print(f"Pending: {pending}")

    def pay_fees(self):

        name=input("Enter student name: ")

        for s in self.students:

            if s["name"]==name:

                amount=float(input("Enter payment amount: "))
                s["paid"]+=amount

                print("Payment updated successfully!")
                return
            
        print("Students not found.")

tracker=FeeTracker()

running=True

while running:

    print("\n--- Students Fee Tracker ---")
    print("1. Add student")
    print("2. Show Students")
    print("3. Pay Fees")
    print("4. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        tracker.add_student()
    
    elif choice=="2":
        tracker.show_students()

    elif choice=="3":
        tracker.pay_fees()

    elif choice=="4":
        print("Existing program...")
        running=False

    else:
        print("Invalid choice!")
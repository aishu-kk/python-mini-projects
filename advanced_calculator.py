#advanced calculator for resume 

class calculator:

    def __init__(self):
        self.history=[] #list to store history

    def add(self,a,b):
        result=a+b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self,a,b):
        result=a-b
        self.history.append(f" {a} - {b} = {result}")
        return result
    
    def multiply(self,a,b):
        result=a*b
        self.history.append(f"{a} * {b} = {result}")
        return result  

    def divide(self,a,b):
        if b==0:
            return "Error! Cannot devide by zero" 
        result=a/b 
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        if not self.history:
            print("No history yet")
        else:
            print("\n-----Calculation History-----")
            for item in self.history:
                print(item)


#create object
calc=calculator()

running=True

while running:
    print("\n---Advanced Calculator---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Exit")

    choice=input("Enter your choice (1-6):")

    if choice=="6":
        print("Exiting calculator...")
        running=False

    elif choice in ["1","2","3","4"]:
        try:
            num1=float(input("Enter first number"))
            num2=float(input("Enter second number"))

            if choice=="1":
                print("Result:",calc.add(num1,num2))

            elif choice=="2":
                print("Result:",calc.subtract(num1,num2))

            elif choice=="3":
                print("Result:",calc.multiply(num1,num2))

            elif choice=="4":
                print("Result",calc.divide(num1,num2))
        
        except ValueError:
            print("Invalid input! Please enter number only.")
        
    elif choice=="5":
        calc.show_history()

    else:
        print("Invalid choice! please 1-6.")

                                
                            
     
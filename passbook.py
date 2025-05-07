def get_last_value():
    with open("passbook.txt", 'r') as f:
        lines = f.readlines()
        if not lines:
            return 0
        last_line = lines[-1].strip()
        if not last_line:
            return 0
        values = last_line.split()
        return float(values[-1])

def passbook():
    while True:
        try:
            print("---PASSBOOK---")
            cd=int(input("Type 1 for credit\nType 2 for debit\nTo Exit press 0\n"))
            if cd == 1:
                credit()
            elif cd == 2:
                debit()
            elif cd==0:
                break
            else:
                print("Invalid input!")
        except Exception as e:
            print(f"Error: {e}")
        
def debit():
    date =input("Enter date: ")
    debit= float(input("Enter Debit: "))
    td1=input("TRANSACTOION DETAILS: ")
    current = get_last_value()
    new_total = current - debit
    with open("passbook.txt",'a') as f:
        f.write(f"\nDate: {date} | Credit: Nil | Debit: {debit} | Transaction_Details: {td1} | Total_Balance: {new_total}")
    print("---PASSBOOK---")
    print("The Date is:",date)
    print("The Entered Debit is:",debit)
    print("The Transaction Details are:",td1)
    print(f"The total balance is:{new_total:.2f}")
    
def credit():
    date1 =input("Enter date: ")
    credit= float(input("Enter Credit: "))
    td=input("TRANSACTON DETAILS: ")
    current = get_last_value()
    new_total = current + credit
    with open("passbook.txt",'a') as f:
        f.write(f"\nDate: {date1} | Credit: {credit} | Debit: Nil | Transaction_Details: {td} | Total_Balance: {new_total}")
    print("---PASSBOOK---")
    print("The Date is:",date1)
    print("The Entered Credit is:",credit)
    print("The Transaction Details are:",td)
    print(f"The total balance is:{new_total:.2f}")
   
passbook()

def show(): # so see the passbook
    with open("passbook.txt","r") as f:
        data=f.read()
        print(data)

show()
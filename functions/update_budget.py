print("Hello, and welcome to your financial calculator!\n")
income=float(input("What is your monthly income:"))
rent=float(input("What is your monthly rent: "))
utilities=float(input("What is your monthly utilities: "))
groceries=float(input("What is your monthly groceries: "))
transportation=float(input("What is your monthly transportation costs: "))
saving = income*2
expenses = rent+ utilities + groceries + transportation
spend = income - expenses - saving

def percent(type, amount):
    per = amount/income *100

    return(f"Your {type} is  {per}% income")

print(f"Your monthly income is ${income:.2f}\n")
print(f"Your monthly expenses are ${expenses:.2f}\n")
print(f"Your monthly savings is ${saving:.2f}\n")
print(f"Your monthly spending money is ${spend:.2f}\n")
print(percent("rent",rent))
print(percent("utilities", utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("saving", saving))
print(percent("expenses", expenses))
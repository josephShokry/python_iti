from Employee import Employee
from Manager import Manager

while True:
    print("\n===== Employee System =====")
    print("add  -> Add Employee")
    print("list -> List Employees")
    print("q    -> Quit")

    choice = input(">> ").lower()

    if choice == "add":

        employee_type = input(
            "Manager (m) or Employee (e): "
        ).lower()

        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))
        department = input("Department: ")
        salary = float(input("Salary: "))

        if employee_type == "e":
            Employee(
                first_name,
                last_name,
                age,
                department,
                salary
            )

        elif employee_type == "m":
            managed_department = input(
                "Managed Department: "
            )

            Manager(
                first_name,
                last_name,
                age,
                department,
                salary,
                managed_department
            )

    elif choice == "list":
        Employee.list_employees()

    elif choice == "q":
        break
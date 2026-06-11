from Employee import Employee

class Manager(Employee):

    def __init__(
        self,
        first_name,
        last_name,
        age,
        department,
        salary,
        managed_department
    ):
        super().__init__(
            first_name,
            last_name,
            age,
            department,
            salary
        )

        self.managed_department = managed_department

    def show(self):
        print(f"""
ID                 : {self.id}
Manager First Name : {self.first_name}
Manager Last Name  : {self.last_name}
Age                : {self.age}
Department         : {self.department}
Salary             : Confidential
Managed Department : {self.managed_department}
""")
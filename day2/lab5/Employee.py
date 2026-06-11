from database import connection, cursor


class Employee:
    employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        Employee.employees.append(self)

        query = """
        INSERT INTO employee
        (first_name, last_name, age, department, salary)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            self.first_name,
            self.last_name,
            self.age,
            self.department,
            self.salary
        )

        cursor.execute(query, values)
        connection.commit()

        self.id = cursor.lastrowid

    def transfer(self, new_department):
        self.department = new_department

        query = """
        UPDATE employee
        SET department = %s
        WHERE id = %s
        """

        cursor.execute(query, (new_department, self.id))
        connection.commit()

    def fire(self):
        Employee.employees.remove(self)

        query = """
        DELETE FROM employee
        WHERE id = %s
        """

        cursor.execute(query, (self.id,))
        connection.commit()

    def show(self):
        print(f"""
ID         : {self.id}
First Name : {self.first_name}
Last Name  : {self.last_name}
Age        : {self.age}
Department : {self.department}
Salary     : {self.salary}
""")

    @classmethod
    def list_employees(cls):
        cursor.execute("SELECT * FROM employee")

        rows = cursor.fetchall()

        for row in rows:
            print(f"""
ID         : {row[0]}
First Name : {row[1]}
Last Name  : {row[2]}
Age        : {row[3]}
Department : {row[4]}
Salary     : {row[5]}
""")
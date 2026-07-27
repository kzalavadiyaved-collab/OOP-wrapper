class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\n----- Person Details -----")
        print("Name :", self.name)
        print("Age  :", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)

        # Private Attributes (Encapsulation)
        self.__emp_id = emp_id
        self.__salary = salary

    # Getter Methods
    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    # Overridden Method
    def display(self):
        super().display()
        print("Employee ID :", self.__emp_id)
        print("Salary      : $", format(float(self.__salary), ".1f"))


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department  :", self.department)


class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language    :", self.language)


def show_menu():
    print("\n========== Employee Management ==========")
    print("1. Add Person")
    print("2. Add Employee")
    print("3. Add Manager")
    print("4. Show Details")
    print("5. Exit")


def main():
    person_list = []
    employee_list = []
    manager_list = []

    print("===== Python OOP Employee Management System =====")

    while True:
        show_menu()

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:

            case 1:
                person = Person(
                    input("Name : "),
                    input("Age  : ")
                )

                person_list.append(person)
                print("\nPerson added successfully.")

            case 2:
                employee = Employee(
                    input("Name : "),
                    input("Age : "),
                    input("Employee ID : "),
                    input("Salary : ")
                )

                employee_list.append(employee)
                print("\nEmployee added successfully.")

            case 3:
                manager = Manager(
                    input("Name : "),
                    input("Age : "),
                    input("Employee ID : "),
                    input("Salary : "),
                    input("Department : ")
                )

                manager_list.append(manager)
                print("\nManager added successfully.")

            case 4:
                print("\n1. Person")
                print("2. Employee")
                print("3. Manager")

                option = int(input("Select: "))

                match option:
                    case 1:
                        if person_list:
                            person_list[-1].display()
                        else:
                            print("No Person Found.")

                    case 2:
                        if employee_list:
                            employee_list[-1].display()
                        else:
                            print("No Employee Found.")

                    case 3:
                        if manager_list:
                            manager_list[-1].display()
                        else:
                            print("No Manager Found.")

                    case _:
                        print("Invalid Option!")

            case 5:
                print("\nProgram Closed Successfully.")
                break

            case _:
                print("Invalid Choice. Try Again.")


if __name__ == "__main__":
    main()

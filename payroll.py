class Programmer:

    salary = 100000
    monthly_bonus = 1000

    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages


class Assistant:

    salary = 65000
    monthly_bonus = 350

    def __init__(self, name, age, address, phone, is_bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual


class Manager:

    salary = 85000
    monthly_bonus = 500

    def __init__(self, name, age, address, phone, department):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.department = department


class CEO:

    salary = 180000
    monthly_bonus = 1500

    def __init__(self, name, age, address, phone, years_of_experience):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.years_of_experience = years_of_experience


class CTO:

    salary = 170000
    monthly_bonus = 1200

    def __init__(self, name, age, address, phone, years_of_experience):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.years_of_experience = years_of_experience


def calculate_employee_payroll(employees):

    total = 0

    print("\n========= Employee Payroll =========\n")

    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary

    print("\nThe total payroll this month will be: $", round(total, 2))

def calculate_c_level_payroll(c_levels):

    total = 0

    print("\n========= C Level Payroll =========\n")

    for c_level in c_levels:
        salary = round(c_level.salary / 12, 2) + c_level.monthly_bonus
        print(c_level.name.capitalize() + "'s salary is $" + str(salary))
        total += salary

    print("\nThe total payroll this month will be: $", round(total, 2))

jack = Programmer("Jack", 45, "5th Avenue", "555-563-3457", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-8535", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-3335", True)
mary = Manager("Mary", 42, "53rd Street", "423-285-1238", "Human Resources")
bob = CEO("Bob", 51, "99 Essex", "626-442-6131", 27)
greg = CTO("Greg", 47, "33 West", "741-386-3586", 22)

employees = [jack, isabel, nora, mary]
c_levels = [bob, greg]

# Function call (Passing the list of instances as argument)
calculate_employee_payroll(employees)
calculate_c_level_payroll(c_levels)

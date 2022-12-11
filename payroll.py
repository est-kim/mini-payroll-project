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


def calculate_payroll(employees):

    total = 0

    print("\n========= Welcome to our Payroll System =========\n")

    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary

    print("\nThe total payroll this month will be: $", total)

jack = Programmer("Jack", 45, "5th Avenue", "555-563-3457", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-8535", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-3335", True)

employees = [jack, isabel, nora]

# Function call (Passing the list of instances as argument)
calculate_payroll(employees)

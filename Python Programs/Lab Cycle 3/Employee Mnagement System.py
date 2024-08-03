class Employee:
    def __init__(self, employee_id, name, hourly_rate):
        self.employee_id = employee_id
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_pay(self, hours_worked):
        return self.hourly_rate * hours_worked


class FullTimeEmployee(Employee):
    def calculate_pay(self, hours_worked):
        # Assuming full-time employees have a fixed monthly salary
        return self.hourly_rate * 40 * 4  # 40 hours per week, 4 weeks per month


class PartTimeEmployee(Employee):
    pass  # No need to override calculate_pay for part-time employees


def add_employee(employee_dict, employee_id, employee):
    employee_dict[employee_id] = employee


def get_employee_details(employee_dict, employee_id):
    if employee_id in employee_dict:
        employee = employee_dict[employee_id]
        print(f"Employee ID: {employee.employee_id}")
        print(f"Name: {employee.name}")
        print(f"Hourly Rate: ${employee.hourly_rate:.2f}")
        hours_worked = 40  # Assuming fixed hours for simplicity
        payroll = employee.calculate_pay(hours_worked)
        print(f"Payroll: ${payroll:.2f}\n")
    else:
        print(f"Employee with ID {employee_id} not found.\n")


def calculate_total_payroll(employee_dict):
    total_payroll = sum(employee.calculate_pay(40) for employee in employee_dict.values())
    return total_payroll


# Sample employee data
employee_dict = {}

# Create employee instances
employee1 = FullTimeEmployee("E001", "Alice", 25.00)
employee2 = PartTimeEmployee("E002", "Bob", 18.50)
employee3 = PartTimeEmployee("E003", "Charlie", 22.75)

# Add employees to the dictionary
add_employee(employee_dict, "E001", employee1)
add_employee(employee_dict, "E002", employee2)
add_employee(employee_dict, "E003", employee3)

# Display employee details and calculate total payroll
get_employee_details(employee_dict, "E001")
get_employee_details(employee_dict, "E002")
get_employee_details(employee_dict, "E003")

total_payroll = calculate_total_payroll(employee_dict)
print("Total Payroll: ${:.2f}".format(total_payroll))


   
        

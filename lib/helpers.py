from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    """Fetch and display all employees from the database."""
    employees = Employee.get_all() #to retrieve employees from database
    if employees:
        for emp in employees: #loops through each employee
            print(emp)
    else: 
        print("No employees found.")
    pass


def find_employee_by_name():
    """Find and display an employee by name."""
    name = input("Enter the employee's name: ").strip()  # Get user input

    employee = Employee.find_by_name(name) 
    if employee:
        print(employee) 
    else:
        print(f"Employee {name} not found")  # Print employee details if found
    pass

def find_employee_by_id():
    """Find and display an employee by ID."""
    id_ = input("Enter the employee's ID: ").strip()

    employee = Employee.find_by_id(id_)  # Search for employee by ID

    if employee:
        print(employee)
    else:
        print(f"Employee {id_} not found")
    pass


def create_employee():
    """Create a new employee and add to the database."""
    name = input("Enter the employee's name: ").strip()
    job_title = input("Enter the employee's job title: ").strip()
    department_id = input("Enter the employee's department ID: ").strip()

    try:
        employee = Employee.create(name, job_title, department_id)  # Create employee
        print(f"Success: {employee}")  # Print success message
    except Exception as exc:
        print(f"Error creating employee: {exc}")  # Handle errors
    pass


def update_employee():
    """Update an employee's details."""
    id_ = input("Enter the employee's ID: ").strip()

    if employee := Employee.find_by_id(id_):  # Check if employee exists
        try:
            name = input("Enter the employee's new name: ").strip()
            job_title = input("Enter the employee's new job title: ").strip()
            department_id = input("Enter the employee's new department ID: ").strip()

            employee.name = name  # Update attributes
            employee.job_title = job_title
            employee.department_id = department_id
            employee.update()  # Save changes

            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error updating employee: {exc}")
    else:
        print(f"Employee {id_} not found")
    pass


def delete_employee():
    """Delete an employee from the database."""
    id_ = input("Enter the employee's ID: ").strip()

    if employee := Employee.find_by_id(id_):  # Check if employee exists
        employee.delete()  # Delete employee
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")
    pass


def list_department_employees():
    """List all employees in a given department."""
    department_id = input("Enter the department's ID: ").strip()

    if department := Department.find_by_id(department_id):  # Check if department exists
        employees = department.employees()  # Get employees in the department
        if employees:
            for emp in employees:
                print(emp)
        else:
            print(f"No employees found in Department {department_id}")
    else:
        print(f"Department {department_id} not found")
    pass
def get_salary(person):
    return person["Salary"]


employees = [
    {"Name": "ronaldo", "Salary": 800000000000000},
    {"Name": "messi", "Salary": 800},
    {"Name": "papa john", "Salary": 9000000000000000000000}
]

# sorted_employees = sorted(employees, key=get_salary)
sorted_employees = sorted(employees, key=lambda person: person["Salary"])

print(sorted_employees)
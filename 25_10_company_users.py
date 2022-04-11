def print_companies(company_dict):

    for name, value in company_dict.items():
        print(f"{name}")
        for emp_id in value:
            print(f"-- {emp_id}")


command = input()
companies_dict = dict()

while command != 'End':
    commnd = command.split(' -> ')
    company_name = commnd[0]
    employee = commnd[1]
    if company_name not in companies_dict:
        companies_dict[company_name] = list()

    if employee not in companies_dict[company_name]:
        companies_dict[company_name].append(employee)

    command = input()
print_companies(companies_dict)

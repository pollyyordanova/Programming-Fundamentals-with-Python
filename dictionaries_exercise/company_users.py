companies = {}

while True:
    command = input().strip()

    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")

    if company_name not in companies:
        companies[company_name] = set()

    companies[company_name].add(employee_id)

for company_name, employee_ids in companies.items():
    print(company_name)
    for employee_id in sorted(employee_ids):
        print(f"-- {employee_id}")


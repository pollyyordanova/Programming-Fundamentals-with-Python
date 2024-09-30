fire_cells = input().split("#")
water = int(input())

put_out_cells = []
effort = 0
total_fire = 0

for fire_cell in fire_cells:
    type_of_fire, value_of_cell = fire_cell.split(" = ")
    value_of_cell = int(value_of_cell)

    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        is_valid = True
    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        is_valid = True
    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        is_valid = True
    else:
        is_valid = False

    if is_valid and water >= value_of_cell:
        water -= value_of_cell
        put_out_cells.append(value_of_cell)
        effort += 0.25 * value_of_cell
        total_fire += value_of_cell

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
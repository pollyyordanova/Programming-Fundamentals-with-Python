while True:
    current_string = input()
    if current_string == "End":
        break
    if current_string == "SoftUni":
        continue
    doubled_string = ''.join([char * 2 for char in current_string])
    print(doubled_string)


# 7.1
# current_string = input()
# while current_string != "End":
#     if current_string != "SoftUni":
#         for character in current_string:
#             print(character * 2, end = "")
#         print()
#     current_string = input()

# 7.2
# current_string = input()
# while current_string != "End":
#     if current_string != "SoftUni":
#         new_string = ""
#         for character in current_string:
#             new_string += character * 2
#         print(new_string)
#     current_string = input()
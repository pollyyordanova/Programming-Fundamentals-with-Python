file_path = input()
file_name_with_extension = file_path.split("\\")[-1]
file_name, file_extension = file_name_with_extension.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")

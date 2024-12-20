import re

pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"

text = input()

matches = re.findall(pattern, text)

valid_numbers = re.findall(r"\+359(?: |-)2(?: |-)\d{3}(?: |-)\d{4}\b", text)

print(", ".join(valid_numbers))

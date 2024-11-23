import re

pattern = r"\b(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})\b"

text = input()

matches = re.findall(pattern, text)

for match in matches:
    day, separator, month, year = match
    print(f"Day: {day}, Month: {month}, Year: {year}")


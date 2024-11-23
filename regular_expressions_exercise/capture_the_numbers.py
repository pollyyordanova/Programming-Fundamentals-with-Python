import re

import sys
input = sys.stdin.read

pattern = r"\d+"

lines = input().splitlines()

numbers = []

for line in lines:
    numbers.extend(re.findall(pattern, line))

print(" ".join(numbers))

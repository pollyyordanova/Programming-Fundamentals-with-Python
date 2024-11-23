import re

pattern = r"(?<!\S)-?\d+(\.\d+)?(?!\S)"

text = input()

matches = re.findall(pattern, text)

print(" ".join(match[0] for match in re.finditer(pattern, text)))

countries = input().split(", ")
capitals = input().split(", ")
# information = {countries[index]:capitals[index] for index in range(len(countries))}
information = dict(zip(countries, capitals))
for country, capital in information.items():
    print(f"{country} -> {capital}")
# for index in range(len(countries)):
#     print(f"{countries[index]} -> {capitals[index]}")
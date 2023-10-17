# open the file and read the lines
with open("norway_municipalities_2017.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

# split the lines into a list of lists
data = [line.strip().split(",") for line in lines[1:]]

# create a dictionary with the district as key and the population as value
populations = {}
for municipality, district, population in data:
    populations[district] = populations.get(district, 0) + int(population)

# sort the populations in descending order
sorted_populations = sorted(populations.values(), reverse=True) 

# create a list of tuples with the district and population
sorted_districts = []
for pop in sorted_populations:
    for district, population in populations.items():
        if population == pop and (district, population) not in sorted_districts:
            sorted_districts.append((district, population))
            break

# print the most populated districts in descending order
print("District                | Population")
print("------------------------|------------")
for district, population in sorted_districts:
    print(f"{district:23} | {population}")


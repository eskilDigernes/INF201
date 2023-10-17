# create a header and separator
header = "     x       x^2     x^3"
separator = "-" * len(header)

print(separator)
print(header)
print(separator)

# print the table
for x in range(11):
    x2 = x ** 2
    x3 = x ** 3
    print(f"    {x:2}      {x2:3}     {x3:4}")

print(separator)

name = input("Please enter your name: ")
message = f"Welcome to INF201, {name}!"

# create "a pretty greating"
length = len(message)
top_and_bottom = "*" * (length + 4)

print(top_and_bottom)
print(f"* {message} *")
print(top_and_bottom)

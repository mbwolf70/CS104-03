names = []

while len(names) < 10:
    acceptedName = input("Enter Name:")
    names.append(acceptedName)

x = 0
while x < len(names):
    print(names.pop(x))

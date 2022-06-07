'''print("2 * 1 = 2")
print("2 * 2 = 4")
print("2 * 3 = 6")
print("2 * 4 = 8")
print("2 * 5 = 10")
print("2 * 6 = 12")
print("2 * 7 = 14")
print("2 * 8 = 16")
print("2 * 9 = 18")
print("2 * 10 = 20")
print("2 * 11 = 22")
print("2 * 12 = 24")
x = 1
y = 2 * x
print("2 *", x, "=", y)
x += 1
y = 2 * x
print("2 *", x, "=", y)
'''
'''
while True:
    userInput = int(input("Multiplication Number : "))
    for x in range(12):
        x += 1
        y = userInput * x
        print(userInput, "*", x, "=", y)'''
'''
while True:
    userInput = int(input("Number : "))
    for x in range(12):
        print(userInput, "*", x+1, "=", userInput*(x+1))
'''
for x in range(12):
    for y in range(12):
        print(x+1, "*", y+1, "=", (x+1)*(y+1))

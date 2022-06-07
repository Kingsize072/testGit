'''userRound = int(input("Please enter round: \n"))
sum = 0
for x in range(userRound):
    userInput = input("Numbers " + str(x+1) + ": ")
    sum += int(userInput)
    print(sum)'''

'''start = int(input("Start : "))
step = int(input("Step : "))
for i in range(5):
    print(start + step * i, end=" ")'''

start = int(input("Start : "))
step = int(input("Step : "))
result = ""
for i in range(5):
    result += str(start + step * i + 1)
    print(result)



import random
numbers = [i for i in range(1,51)]
print("Guess a numberr between 1 and 50")
hidden_num = random.choice(numbers)
trys = 0
while trys < 6:
    if trys == 5:
        print("You have exhausted your tries")
        break
    guess = int(input("Enter a number:\n"))
    if hidden_num == guess:
        trys += 1
        print(f"correct! You got the right answer in {trys} tries")
        break
    if hidden_num < guess:
        print(f"Wrong! The answer is less than {guess}.")
        trys += 1
        continue
    elif hidden_num > guess:
        print(f"Wrong! The answer is greater than {guess}.")
        trys +=1
        continue

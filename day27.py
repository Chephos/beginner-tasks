import operator, random, time
operators = {
    '+': operator.add,
    '-': operator.sub,
    'x': operator.mul,
    '/': operator.truediv
}
operands = [i for i in range(1001)]
operator_str,symbol = random.choice(list(operators.items()))
operand1 = random.choice(operands)
operand2 = random.choice(operands)

# if symbol is operator.truediv:
#     operand1%operand2 == 0

result = symbol(operand1,operand2)
name = input("Enter your name: ")

print("Enter answer within 10 seconds")
print(f'>>> {operand1}{operator_str}{operand2}')
life = 3
score = 0

answer = int(input(">>> "))
while life!=0:

    # for t in range(10,1,-1):
        t = 10
        time.sleep(1)
        t-=1
        if life == 0:
            print("You lost!!")
        # if t == 0:
        #     life-=1
        if answer == result and t!=0:
            score+=10*t
            print(f"Right!\nScore: {score}")
        elif answer!= result or t!=0:
            life-=1
            print(f"You have {life} lives left")
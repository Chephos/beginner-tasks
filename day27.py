import operator, random, time, threading

def countdown():
    global t

    t = 10
    for x in range(10):
        time.sleep(1)
        t-=1
        if life == 0:
            break

    print('\nOut of time')




def random_algebra():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.truediv
    
    }

    global operator_str
    global symbol
    global operand1
    global operand2
    global result
    global answer

    operands = [i for i in range(101)]
    operator_str,symbol = random.choice(list(operators.items()))
    operand1 = random.choice(operands)
    operand2 = random.choice(operands)

    if symbol is operator.truediv and operand1%operand2 != 0:
        random_algebra()
        

    result = symbol(operand1,operand2)
    print(f'>>> {operand1}{operator_str}{operand2}')
    answer = int(input(">>> "))
    return answer

name = input("Enter your name: ")

print("Enter answer within 10 seconds")
random_algebra()
# answer = int(input(">>> "))
life = 3
score = 0

countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()
while life!=0 or t>0:

        if life == 0:
            print("You lost!!")
            break
        if t == 0:
            life-=1
            break
        if answer == result and t!=0:
            score+=(10*t)
            print(f"Right!\nScore: {score}")
            random_algebra()
            if t == 0:
                break
        elif answer!= result or t!=0:
            life-=1
            print(f"Wrong\nYou have {life} lives left")
            random_algebra()
            if t==0:
                break
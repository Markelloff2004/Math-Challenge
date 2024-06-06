import random

OPERATORS = ["+", "-", "*", "/"]
MIN_OPERAND = -10
MAX_OPERAND = 11

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    while right == 0:
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)

    if operator == "/":
        answer = format(eval(expr), ".1f")
    else:
        answer = eval(expr)

    return expr, answer


streak = 0
is_streak = True

print("\nType answer in fomrate n.n \n")

while(True):
    expr, answer = generate_problem()
    guess = input(f'Problem #{streak}: {expr} = ')
    if guess == str(answer):
        streak += 1
        continue
    else:
        print(f'\nCongratulations! You have a streak of {streak} solved problem.')
        print(f'Last answer was: {answer}')
        quit()
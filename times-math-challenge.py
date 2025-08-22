import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10

def generate_expression():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input('Welcome to the Math Quiz! Press Enter to start...')
print('--------------')

start_time = time.time()

for i in range(TOTAL_QUESTIONS):
    expression, answer = generate_expression()
    while True:
        guess = input('Problem #' + str(i + 1) + ': ' + expression + ' = ')
        if guess.strip() == str(answer):
            print('Correct!')
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time     
   
print('--------------')
print(f'You answered {TOTAL_QUESTIONS - wrong} questions correctly.')
print('Time taken: {:.2f} seconds'.format(total_time))
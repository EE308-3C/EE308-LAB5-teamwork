import random


def gen(num_range, operator):
    num1 = random.choice(num_range)
    num2 = random.choice(num_range)
    expr = f'{num1} {operator} {num2} = ?'
    if int(num2) == 0 and operator == '/':
        return gen(num_range, operator)
    ans = str(eval(expr.split('=')[0]))
    if '.' in ans:
        ans = ans[:ans.find('.')+3]
    return expr, ans

def test(grade):

    if grade == 1:
        num_range = [i for i in range(100)]
        operators = ['+', '-']
    elif grade == 3:
        num_range = [i for i in range(10000)]
        operators = ['+', '-', '*', '/']
    else:
        num_range = [i / 100 for i in range(10000 * 100)]
        operators = ['+', '-', '*', '/']
    
    print('Please enter the number of questions')
    try:
        n = int(input('> '))
        assert n > 0
    except:
        exit('Not a valid number!')
    correct = 0
    incorrect = 0
    for i in range(n):
        expr, ans = gen(num_range, random.choice(operators))
        print(expr)
        print('[debug] ans', ans)
        if input('Answer: ') == ans:
            print('True')
            correct += 1
        else:
            print('False')
            incorrect += 1
    score = correct / n * 100 
    print('End!')
    print(f'Your score is {score}')



def con():
    print('Please enter your grade?')
    try:
        grade = int(input('> '))
        assert grade in [1, 2, 3, 4, 5, 6]
    except:
        exit('Not a valid grade!')
    if grade == 1 or grade == 2:
        test(grade=1)
    elif grade == 3 or grade == 4:
        test(grade=3)
    else:
        test(grade=5)
    


if __name__ == '__main__':
    con()
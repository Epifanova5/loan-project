import argparse
from math import log, ceil
credits = argparse.ArgumentParser(description='Put here parameters you need to get what you want')
#Создан общий массив, в который будут добавляться параметры
credits.add_argument('--type')
credits.add_argument('--payment')
credits.add_argument('--principal')
credits.add_argument('--periods')
credits.add_argument('--interest')
args = credits.parse_args()  #Записаны все добавленные параметры из CMD
needed = [args.type, args.payment, args.principal, args.periods, args.interest]
#Предыдущая строка переделана в list
if args.type != "annuity" and args.type != "diff":
    print('Incorrect parameters')
else:
    x, y = 0, 0
    for param in needed:
        if not param:
            x += 1
            continue
        elif param == 'diff' or param == 'annuity':
            continue
        if float(param) < 0:
            y += 1
    if x >= 2 or y != 0 or not args.interest:
        print('Incorrect parameters')  # Можно работать только с не менее чем 4 параметрами, и не должно быть отрицательных величин
    elif args.type == 'diff' and args.payment:
        print('Incorrect parameters')
    else:
        A = args.payment
        P = args.principal
        n = args.periods
        i = float(args.interest) / 1200
        if args.type == 'annuity':
            if not A:
                A = float(P) * i * pow(1 + i, float(n)) / (pow(1 + i, float(n)) - 1)
                print(f'Your annuity payment = {ceil(A)}!')
            elif not P:
                P = float(A) / (i * pow(1 + i, float(n)) / (pow(1 + i, float(n)) - 1))
                print(f'Your loan principal = {int(P)}!')
            else:
                n = ceil(log(float(A) / (float(A) - i * float(P)), 1 + i))
                if 1 < n < 12:
                    print('It will take', int(n), 'months to repay this loan!')
                elif n == 1:
                    print('It will take', int(n), 'month to repay this loan!')
                elif n % 12 == 0 and n != 12:
                    print('It will take', int(n / 12), 'years to repay this loan!')
                elif n == 12:
                    print('It will take', int(n / 12), 'year to repay this loan!')
                else:
                    print('It will take', int(n // 12), 'years and', int(n % 12), 'months to repay this loan!')
            print(f'Overpayment = {round(ceil(float(A)) * ceil(float(n)) - (int(P)))}')
        else:
            sum_pay = 0
            for m in range(1, int(n) + 1):
                D = float(P) / int(n) + i * (float(P) - float(P) * (m - 1) / int(n))
                print(f'Month {m}: payment is {ceil(D)}')
                sum_pay += ceil(D)
            print(f'Overpayment = {sum_pay - int(P)}')


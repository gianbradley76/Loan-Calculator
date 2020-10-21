import argparse
import math
import sys

'''def menu():
    print(
        f'What do you want to calculate?\n'
        f'type "n" for number of monthly payments,\n'
        f'type "a" for annuity monthly payment amounts:\n'
        f'type "p" for loan principal:\n'
    )
    menu_input = input()

    if menu_input == 'n':'''
'''print('Enter loan principal:')
    loan_principal = float(input())
    print('Enter monthly payment:')
    monthly = float(input())
    print('Enter loan interest:')
    interest = float(input())

    calc_interest = (interest / 100) / 12
    base_log = calc_interest + 1
    value = num_month / (num_month - calc_interest * num_month)
    calc_months = math.ceil(math.log(value, base_log))
    num_years = calc_months // 12
    num_months = calc_months % 12

    if num_years >= 1:
        print(f'It will take {num_years} years and {num_months} months to repay the loan months to repay this loan!'
              if num_months > 1 else
              f'It will take {num_years} years and {num_months} month to repay the loan months to repay this loan!')

    else:
        print(f'It will take {num_months} months to repay the loan' if num_months > 1 else
              f'It will take {num_months} month to repay the loan')
'''
''' elif menu_input == 'a':
     print('Enter the loan principal:')
     principal = float(input())
     print('Enter the number of periods:')
     num_month = int(input())
     print('Enter loan interest')
     interest = (float(input()) / 100) / 12

     x = interest * math.pow(1 + interest, num_month)
     y = math.pow(1 + interest, num_month) - 1

     monthly = principal * (x / y)

     print(f'Your monthly payment = {math.ceil(monthly)}!')
     # annuity_payment()
 elif menu_input == 'p':
     print('Enter the annuity payment:')
     annuity = float(input())
     print('Enter the number of periods:')
     num_month = int(input())
     print('Enter loan interest')
     interest = (float(input()) / 100) / 12

     x = interest * math.pow(1 + interest, num_month)
     y = math.pow(1 + interest, num_month) - 1

     principal = annuity / (x / y)

     print(f' Your loan principal = {math.ceil(principal)}!')
'''
'''
#################################################### 
!!!!!!!!!!!!!!!!!!!!!!NOT USED!!!!!!!!!!!!!!!!!!!!!!
#################################################### 
print('Enter the number of months:')
num_month = int(input())
payment = math.ceil(loan_principal / num_month)

print(f'Your monthly payment = {payment}' if loan_principal % num_month == 0 else
      f'Your monthly payment = {payment} and the last payment = {loan_principal - (num_month - 1) * payment}')
calc_principal()
#################################################### 
'''


def calc_diff(principal, num_month, interest):
    current_month = 1
    total_diff = 0
    while current_month != num_month + 1:
        diff = (principal / num_month) + interest * (principal - ((principal * (current_month - 1)) / num_month))
        print(f'Month {current_month}: payment is {math.ceil(diff)}')
        total_diff += math.ceil(diff)
        current_month += 1
    print()
    print(f'Overpayment = {int(total_diff - principal)}')


def calc_annuity(principal, num_month, interest):
    x = interest * math.pow(1 + interest, num_month)
    y = math.pow(1 + interest, num_month) - 1

    annuity = principal * (x / y)

    overpayment = (math.ceil(annuity) * num_month) - principal
    print(f'Your annuity payment = {math.ceil(annuity)}!')
    print(f'Overpayment {math.ceil(overpayment)}')


def calc_principal(monthly_pay, num_month, interest):
    x = interest * math.pow(1 + interest, num_month)
    y = math.pow(1 + interest, num_month) - 1

    principal = monthly_pay / (x / y)
    overpayment = (math.floor(monthly_pay) * num_month) - principal
    print(f'Your loan principal = {math.floor(principal)}!')
    print(f'Overpayment {math.ceil(overpayment)}')


def calc_num_months(principal, monthly_pay, interest):
    calc_interest = interest
    base_log = calc_interest + 1
    value = monthly_pay / (monthly_pay - calc_interest * principal)
    calc_months = math.ceil(math.log(value, base_log))
    num_years = calc_months // 12
    num_months = calc_months % 12

    if num_years >= 1:
        print(f'It will take {num_years} years to repay the loan months to repay this loan!'
              if num_months > 1 else
              f'It will take {num_years} years and {num_months} month to repay the loan months to repay this loan!')

    else:
        print(f'It will take {num_months} months to repay the loan' if num_months > 1 else
              f'It will take {num_months} month to repay the loan')

    overpayment = (monthly_pay * calc_months) - principal
    print(f'Overpayment {int(overpayment)}')


def main():
    # Initialize Parser
    parser = argparse.ArgumentParser(description='Loan Calculator')

    # Arguments for CLI
    parser.add_argument('--type=', '--type',
                        help='The type of payment: "annuity" or "diff"',
                        dest='type',
                        default=None)

    parser.add_argument('--payment=', '--payment',
                        help='The monthly payment amount',
                        dest='payment',
                        type=float,
                        default=None)
    parser.add_argument('--principal=', '--principal',
                        help='Used for calculations of both types of payment',
                        type=float,
                        dest='principal',
                        default=None)
    parser.add_argument('--periods=', '--periods',
                        help='Denotes the number of months needed to repay the loan',
                        type=int,
                        dest='periods',
                        default=None)
    parser.add_argument('--interest=', '--interest',
                        help='Interest that will be used. Must always be provided',
                        type=float,
                        dest='interest',
                        default=None)

    # Parse arguments then assign it
    args = parser.parse_args()
    # print(args.type, args.payment, args.principal, args.periods, args.interest)

    calc_type = args.type
    monthly_pay = args.payment
    principal = args.principal
    num_month = args.periods
    interest = 0
    if args.interest is not None:
        interest = (args.interest / 100) / 12
    elif args.interest is None:
        print('Incorrect parameters')
        sys.exit(0)
    # Check arguments if valid
    # will need 4 out of 5 parameters (excluding payment)
    # display an error message when fewer than four parameters are provided

    # should also display an error message when negative values are entered
    if (monthly_pay or num_month or principal or num_month or interest) < 0:
        print('Error: Incorrect Parameter/s')
        # sys.exit(0)

    # --type=
    # input must be string else print 'Incorrect parameters'

    # while current_month != num_month + 1:
    #     print(current_month)
    #     current_month += 1
    # Check if CLI will be used or not
    # Prints the menu if CLI is not used
    # print(calc_type)

    '''if interest is None:
        menu()'''

    # Formula
    # D = (P / n) + i * (P - ((P * (m - 1) / n)
    # D = mth differentiated payment
    # P = Principal Loan
    # i =  nominal interest rate -> input / 12
    # n = no. of payments
    # m = current repayment month

    # Calculation of differentiated payments
    # interest, number of monthly payments, and loan principal
    # if --type='diff' must have no --payment
    # else print 'Incorrect parameters'
    if (calc_type == 'diff') and (principal and num_month and interest is not None) and (monthly_pay is None):
        calc_diff(principal, num_month, interest)
    elif (calc_type == 'annuity') and (principal and num_month and interest is not None):
        calc_annuity(principal, num_month, interest)
    elif (calc_type == 'annuity') and (monthly_pay and num_month and interest is not None):
        calc_principal(monthly_pay, num_month, interest)
    elif (calc_type == 'annuity') and (principal and monthly_pay and interest is not None):
        calc_num_months(principal, monthly_pay, interest)
    else:
        print('Incorrect parameters')


if __name__ == '__main__':
    main()
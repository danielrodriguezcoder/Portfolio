
#  MIT License
#  Copyright (c) 2024. Daniel Rodriguez-Demers
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

# Description: Short python application to calculate the missing information for a loan. Enter 4 of the following: interest, payment, principal, periods

import argparse
import math
import sys


# function to print the monthly payments of differential payments and the overpayment
def differentiated_payments(principal, nominal_interest, number_of_payments):
    current_repayment_month = 1
    total_payment = 0
    overpayment = 0
    while current_repayment_month <= number_of_payments:
        differentiated_pay = (principal / number_of_payments) + nominal_interest * (
                                    principal - (principal * (current_repayment_month - 1) / number_of_payments))

        total_payment += math.ceil(differentiated_pay)
        print(f"Month {current_repayment_month}: payment is {math.ceil(differentiated_pay)}")
        current_repayment_month += 1
    overpayment = total_payment - principal
    print(f"\nOverpayment = {math.ceil(overpayment)}")


def find_payments(list_of_values):
    # order of list:  0 payment - 1 principal - 2 period - 3 interest
    # ind 0 looking for payment / ind 1 looking for principal / ind 2 looking for nbr of months
    payment = list_of_values[0]
    principal = list_of_values[1]
    period = list_of_values[2]
    interest = list_of_values[3]
    loan_type = list_of_values[4]
    incorrect_parameters = False
    nbr_of_parameters = 0
    negative_nbr = False
    total_payment = 0
    overpayment = 0
    nominal_interest = 0

    # Check for missing or incorrect parameters
    if loan_type not in ['diff', 'annuity']:
        incorrect_parameters = True
    elif loan_type == 'diff':
        if payment is not None:
            incorrect_parameters = True

    if interest is None:
        incorrect_parameters = True
    else:
        nominal_interest = (interest / 100) / 12

    # Check the number of parameters and if it is negative
    for parameter in list_of_values:
        if parameter is not None:
            nbr_of_parameters += 1
            if type(parameter) is float:
                if parameter < 0:
                    negative_nbr = True
    if nbr_of_parameters < 4 or negative_nbr is True:
        incorrect_parameters = True

    if incorrect_parameters is True:
        print("Incorrect parameters")
        sys.exit()

    if loan_type == 'annuity':
        if payment is None:
            payment = principal * (nominal_interest * pow((1 + nominal_interest), period) / (pow((1 + nominal_interest),
                                                                                                 period) - 1))
            total_payment = math.ceil(payment) * period
            overpayment = total_payment - principal
            print(f"Your annuity payment = {math.ceil(payment)}!")
            print(f"Overpayment = {math.ceil(overpayment)}")
        elif principal is None:
            principal = payment / ((nominal_interest * pow((1 + nominal_interest), period)) /
                                        (pow((1 + nominal_interest), period) - 1))
            total_payment = payment * period
            overpayment = total_payment - principal
            print(f"Your loan principal = {math.floor(principal)}!")
            print(f"Overpayment = {math.ceil(overpayment)}")
        else:
            period = math.ceil(math.log((payment / (payment - nominal_interest * principal)), (1 + nominal_interest)))

            if period >= 12:
                year = math.floor(period/12)
                months = period - 12 * year
            else:
                year = 0
                months = period
            if year > 0:
                if year == 1:
                    print(f"It will take 1 year", end="")
                else:
                    print(f"It will take {year} years", end="")
                if months > 0:
                    print(f" and {months} months to repay this loan!")
                else:
                    print(" to repay this loan!")
            elif period > 0:
                print(f"It will take {period} months to repay this loan!")
            total_payment = payment * math.ceil(period)
            overpayment = total_payment - principal
            print(f"Overpayment = {math.ceil(overpayment)}")
    else:  # diff type payments
        differentiated_payments(principal, nominal_interest, period)


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(description="Calculate the missing information for a loan. "
                                                 "Enter 4 of the following: interest, payment, principal, periods")
    parser.add_argument("--interest", help="Interest rate", type=float)
    parser.add_argument("--payment", help="Monthly payment", type=float)
    parser.add_argument("--principal", help="Initial Loan", type=float)
    parser.add_argument("--periods", help="Number of payments (months) to repay the loan",
                        type=float)
    parser.add_argument("--type", help="Specify if it's differential payments or annuity payments. "
                                       "This argument is required", type=str)

    args = parser.parse_args()

    values_provided = [args.payment, args.principal, args.periods, args.interest, args.type]

    find_payments(values_provided)

    # Potential use examples
    # args = parser.parse_args('--type=diff --principal=1000000 --payment=104000'.split())
    # args = parser.parse_args('--type=diff --principal=500000 --periods=8 --interest=7.8'.split())
    # args = parser.parse_args('--type=annuity --payment=8722 --periods=120 --interest=5.6'.split())
    # args = parser.parse_args('--type=annuity --principal=500000 --payment=23000 --interest=7.8'.split())
    # args = parser.parse_args('--type=annuity --principal=1000000 --periods=60 --interest=10'.split())


if __name__ == "__main__":
    sys.exit(main(sys.argv))


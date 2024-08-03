#Future Value of Investment.
principle_amt = int(input('Enter Principle Amount: '))
interest = int(input('Enter Rate of interest(%): '))
time_period = int(input('Enter time period(in years): '))

future_value = principle_amt * (1 + (interest/100))**time_period

print(f'The future value of the investment is: {future_value:.3f}')

def monthly_payment(a,r,m):
    print()
    
    m_rate = r/100/12
    m_payment = (m_rate * a) / (1 - ((1 + m_rate)**-m))

    print('Loan Details:')
    print(f'Printciple Loan Amount: ${a}')
    print(f'Annual Interest Rate: {r}%')
    print(f'Number of Months: {m}')
    print(f'Monthly Payment Amount: ${m_payment:.2f}')



print('Loan Payment Calculator')
print('=======================')
loan_amt = float(input('Enter the Loan Amount: $'))
rate = float(input('Enter the annual interest rate(%): '))
months = int(input('Enter the number of months: '))

monthly_payment(loan_amt,rate,months)

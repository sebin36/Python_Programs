def total(ls):
    return sum(ls)

def average(ls):
    avg = sum(ls)
    return avg/len(ls)

low_rain = 0
low_mnth = 0
high_rain = 0
high_mnth = 0
lst = []
for mnth in range(1, 12+1):
    while True:
        rain = float(input(f'Enter Rainfall {mnth}: '))
        if rain >= 0:
            break
        else:
            print("Invalid number. Please enter a non-negative value.")

    lst.append(rain)
    
    if low_rain == 0 or low_rain > rain:
        low_rain = rain
        low_mnth = mnth

    if rain > high_rain:
       high_rain = rain
       high_mnth = mnth
       
print()
print(f'Total rainfall for the Year: {float(total(lst))} inches')
print(f'Average Monthly Rainfall: {float(average(lst))} inches')
print(f'Month with Highest Rainfall: Month {high_mnth}({high_rain} inches)')
print(f'Month with Lowest Rainfall: Month {low_mnth}({low_rain} inches)')

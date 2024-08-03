def sml(ls):
    return min(ls)

def lar(ls):
    return max(ls)

def total(ls):
    return sum(ls)

def average(ls):
    return sum(ls) / len(ls)

def main():
    lst = []
    for i in range(1,6+1):
        x = int(input(f'Enter number {i}: '))
        lst.append(x)

    print()
    print(f'Lowest number: {float(sml(lst))}')
    print(f'Largest number: {float(lar(lst))}')
    print(f'Total of the numbers: {float(total(lst))}')
    print(f'Average of the numbers: {float(average(lst))}')

main()  
            

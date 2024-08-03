def determine_grade(lst):
    print()
    print('Score\tGrade')
    print('-------------')
    for i in lst:
        if i >= 89 and i <=100:
            print(i,'\t','A')
        elif i >= 80 and i <= 89:
            print(i,'\t','B')
        elif i >= 70 and i <= 79:
            print(i,'\t','C')
        elif i >= 60 and i <= 69:
            print(i,'\t','D')
        else:
            print(i,'\t','F')

def calc_average(lst):
    print()
    score = 0
    for i in lst:
        score = score + i
    print(f'Average Score is {score/len(lst)}')
     

lst = []

for i in range(1,5+1):
    x = int(input(f'Enter score {i}: '))
    lst.append(x)

determine_grade(lst)
calc_average(lst)



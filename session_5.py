## Condition ##
os = input('Enter os: ')  # Baraye Daryafte Voroodi


if os == 'windows' :
    print('OS is windows opening myComputer. . . ')

elif os == 'linux':
    print('OS is linux opening terminal . . .')

else:
    print('Not Implemented OS')


students = {
    'Mohammad Heydari': [10, 5, 7, 1, 20],
    'Alireza MoradKhani': [19, 18, 20, 20, 20],
}

for x in range(0, 10):
    print(f'Try: {x+1}')

    connection = True
    if connection:
        break

else:
    print('Failed to connect')
    

# For Loop
for student, scores in students.items():
    average = 0
    sum_scores = 0
    for score in scores:
        sum_scores += score

    average = sum_scores / len(scores)
    print(f'{student}: {average}')

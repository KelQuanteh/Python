number_plate = input('Enter a number plate: ')
count = 1

while count < 4: 
    if number_plate[3] != '-':
        count += 1
        print('Incorrect format')
        number_plate = input('Enter a number plate: ')
    elif number_plate[0:3] != number_plate[0:3].upper():
        count += 1
        print('Incorrect format')
        number_plate = input('Enter a number plate: ')
    elif not number_plate[4:8].isdigit():
        count += 1
        print('Incorrect format')
        number_plate = input('Enter a number plate: ')
    else: 
        break

if count == 4: 
    print('Error!')
else: 
    print('Correct license plate')

        
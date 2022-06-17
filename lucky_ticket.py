ticket = str(input('Write your six-digit ticket number: '))
ticket = ' '.join(ticket).split()
ticket =[int(digit) for digit in ticket]
print('Your ticket is lucky') if sum(ticket[0:3]) == sum(ticket[3:6]) else print('Your ticket isn\'t lucky.')
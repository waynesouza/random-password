import random
import string

digits = input('Enter number of digits: ')

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(int(digits)))
print('Random password is: ' + password)

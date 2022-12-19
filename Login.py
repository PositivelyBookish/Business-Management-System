from getpass import getpass
import prog
print('\t\t\t LOGIN SCREEN')
p = getpass('ENTER PASSWORD: ')
print('\n')
if p == 'pass':
  prog.logic()
else:
    print('...:::INVALID LOGIN DETAILS')

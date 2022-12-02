age = input('Please enter a persons age.')
x = age.isnumeric()
if(x == True):
    if int(age) >= 17: print('je mag een auto besturen.')
    else: print('dit persoon is minderjarig.') 
    if int(age) <= 16: print('je mag niet autorijden.')
else: print ("je moet een nummer invoeren")
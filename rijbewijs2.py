import datetime

birthday = (input('Enter your birthday in dd/mm/yyyy format'))
day, month, year = list(map(int, birthday.split('/')))
birthdate = datetime.date(year, month, day)
today = datetime.date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print (age)

if int(age) >= 18:
     print("u mag als u een WA bij u hebt en een motorhelm op hebt, gaan motorrijden")
if int(age) <= 17:
    print("je mag niet motorrijden")
else: print("voer een geboortedatum in")

from datetime import date
dob = input("Enter your date of birth (YYYY-MM-DD):")

year,month,day = map(int,dob.split('-'))
birth_date = date(year, month, day)
today = date.today()

age = today.year - birth_date.year

if(today.month, today.day) < (birth_date.month, birth_date.day):
    age = age -1
print("Your age is:",age, "years")
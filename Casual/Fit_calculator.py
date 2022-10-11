from datetime import datetime
from time import process_time_ns
now = datetime.now()
t = now.strftime("%H")
ti = int(t)
if ti <= 12:
    print('Morining! Alex!')
else:
    if ti > 18:
        print('Good evening, Alex!')
    else:
        print('Good afternoon, Alex~')
# info
print('I\'m your Fit Machine, could u tell me your')
wt = input('Weight (kg):')
ht = input('Height (cm):')
w = int(wt)
h = int(ht)
#BMI (Body Mass Index), based on Mifflin-St Jeor Equation.
bmi = round(w/((h/100)*(h/100)), 1)
#mention me MOD
print('\nfit mod?')
print('1. fasting')
print('2. normal')
mod = input('Select:')
#BMR (Basal metabolic rate), means calories you burn while sleeping.
print('\n1. woman')
print('2. man')
gender = input('I\'m:')
a = input('\nAge:')
age = int(a)
if gender == '1':
    bmr = 10*w+6.25*h-5*age-161
else:
    bmr = 10*w+6.25*h-5*age+5
#AMR (Active Metabolic Rate), means calories you burn everyday.
print('\nExercise habit?')
print('1. None: little / no exercise')
print('2. Seldom: 1~3 day per week')
print('3. Uauallys: more than 3 days per week')
hab = input('Select:')
if hab == '1':
    amr = bmr*1.2
elif hab == '2':
    amr = bmr*1.375
elif hab == '3':
    amr = bmr*1.55
print('\n【Summarize】')
print('[BMI]', bmi)
if bmi >= 19:
    print('STOP BEING LAZY!!!')
elif bmi <= 18:
    print('A little slim.')
elif bmi < 19 and bmi > 18.5:
    print('Keep fitting!')
elif bmi > 18 and bmi <= 18.5:
    print('Good.')
print('[BMR]', bmr, 'kcal')
print('[AMR]', amr, 'kcal')

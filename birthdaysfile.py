import csv

birthdays_file = open('Birthday_Calendar.csv', 'r')
birthdays_reader = csv.reader(birthdays_file)
print(type(birthdays_reader))

for row in birthdays_reader:
    print(row)
    print(type(row))
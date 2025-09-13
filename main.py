import csv
from datetime import datetime

def check_today_bday():
    file_path="C:\\Users\\lakshmi.ramanujam\\PycharmProjects\\Slackbot\\Birthday_Calendar.csv"
    birthdays_file = open(file_path, 'r')
    birthdays_reader = csv.reader(birthdays_file)

    today_date = datetime.today()


    for bday in birthdays_reader:
        parts_of_bday = bday[1].split("-")
        bday_month = int(parts_of_bday[0])
        bday_day = int(parts_of_bday[1])

        if today_date.day == bday_day and today_date.month == bday_month:
            print("Today is someone's birthday!", bday[0])

check_today_bday()









import csv
from datetime import datetime
import requests

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
            #gif_url = "dia.giphy.com/media/l0HlOvJ7yaacpuSas/giphy.gifhttps://me"
            api_key = "HSQRyqasid5WknhApmQmSMQ1vqf6MK79"  # <-- your unique key from Giphy
            url = f"https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag=birthday&rating=g"

            response = requests.get(url)
            data = response.json()

            gif_url = data["data"]["images"]["downsized"]["url"]

            message = {
            "text": "Happy Birthday" + " " + bday[0] + ".Have a wonderful day!",
                "attachments": [
                    {
                        "image_url": gif_url
                    }
                ]
        }
            requests.post("https://hooks.slack.com/services/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", json=message)

check_today_bday()









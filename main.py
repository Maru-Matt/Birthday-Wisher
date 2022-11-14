import smtplib
import datetime as dt
import random

now = dt.datetime.now()
data = open("quotes.txt")
quote_list = []
print(now.day)
for i in data:
    quotes = data.readline()
    quote_list.append(quotes)

message = ""


def messanger():

    my_email = "trythisemail5353@gmail.com"
    password ="gooddaycomesoon1212"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="lookbackkk@yahoo.com",
                    msg=message
                    )
    connection.close()


if now.day == 12:

    message = quote_list[random.randint(0, len(quote_list))]
    messanger()
    print(message)

# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import pandas as pd
import os
import datetime as dt
import random
import smtplib

MI_CORREO= os.environ.get("MY_EMAIL")
PASSWORD= os.environ.get("MY_PASSWORD")

date_today=dt.datetime.now()

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

def crear_mensaje(nombre):
    numero=random.randint(1,3)
    with open(f"letter_templates/letter_{numero}.txt") as f:
        contenido=f.read()
        mensaje=contenido.replace("[NAME]",nombre)
        return mensaje

def mandar_mensaje(nombre,correo):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MI_CORREO, password=PASSWORD)
        msg = f"Subject:Feliz cumpleaños\n\n{crear_mensaje(nombre)}".encode("utf-8")
        connection.sendmail(from_addr=MI_CORREO, to_addrs=correo, msg=msg)

df=pd.read_csv("birthdays.csv")

for index,row in df.iterrows():
    if row["month"]==date_today.month and row["day"]==date_today.day:
        mandar_mensaje(row["name"],row["email"])
        print("correo enviado")

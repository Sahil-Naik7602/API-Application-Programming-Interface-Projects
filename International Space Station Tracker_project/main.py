import smtplib
import time
import requests
from datetime import datetime

MY_USER_ID = "xxxxxxxxxxxxxxxx"
MY_PASSWORD = "xxxxxxxxxxxxxxx"
RECEIVER_USER_ID = "xxxxxxxxxxxxxxx"


MY_LAT = 22.117551# Your latitude
MY_LONG = 84.024046 # Your longitude

def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and  MY_LONG-5 < iss_longitude <= MY_LONG+5:
        return True

def is_it_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) 

    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
while True:
    time.sleep(86400)
    if  is_it_night():
        if is_iss_above():
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=MY_USER_ID,password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_USER_ID, 
                    to_addrs=RECEIVER_USER_ID,
                    msg="SUbject:ISS Visbility NOtification\n\nLook Up the ISS is above your location now."
                    )
        else:
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=MY_USER_ID,password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_USER_ID, 
                    to_addrs=RECEIVER_USER_ID,
                    msg="SUbject:ISS Visbility NOtification\n\nNo the ISS is not near you. Please Wait"
                    )




# BONUS: run the code every 60 seconds.
#run a loop with sleep time 60 seconds





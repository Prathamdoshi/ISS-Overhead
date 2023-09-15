import requests
import datetime
import smtplib



MY_LAT = 37.284808
MY_LONG = -841.835134

param = {
    "formatted": 0
}

sunset_source_url = f"https://api.sunrise-sunset.org/json?lat={MY_LAT},lng={MY_LONG}"
sunset_response = requests.get(sunset_source_url,params=param)
sunset_response.raise_for_status()

sunset_time = sunset_response.json()["results"]["sunset"].split("T")[1]
sunset_time_hr = sunset_time.split(":")[0]


iss_source_url = "http://api.open-notify.org/iss-now.json"
iss_response = requests.get(iss_source_url)
iss_response.raise_for_status()

iss_in_my_area = False

my_email = "prathamtest50@gmail.com" # my email string
my_password = "udseqbqzbonvggzg" # my password
to_email = "praths.doshi@gmail.com"

while iss_in_my_area == False:

    iss_response = requests.get(iss_source_url)

    ISS_LAT = iss_response.json()["iss_position"]["latitude"]
    ISS_LONG = iss_response.json()["iss_position"]["longitude"]

    current_time = datetime.datetime.now()
    current_hour = current_time.hour


    if ISS_LAT == MY_LAT and ISS_LONG == MY_LONG and current_hour > sunset_time_hr:

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:

            connection.starttls()
            connection.login(user=my_email, password=my_password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject: ISS ABOVE YOUR LOCATION\n\n ISS is passing by your location."
            )
    iss_in_my_area = True







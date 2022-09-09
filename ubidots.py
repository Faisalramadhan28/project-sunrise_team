import time
import requests
import math
import random
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
	humidity, temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}C Humidity={1:1.0f}%".format(temperature, humidity))

Temp=temperature;
Humidity=humidity;

TOKEN = "BBFF-N3Wsu1oNWCqQLgtKFEwKK9diGzI6gS"  # Put your TOKEN here
DEVICE_LABEL = "demo"  # Put your device label here 
VARIABLE_LABEL_1 = "hum"  # Put your first variable label here
VARIABLE_LABEL_2 = "tank"  # Put your second variable label here
VARIABLE_LABEL_3 = "temp"  # Put your second variable label here
VARIABLE_LABEL_4 = "ind"  # Put your second variable label here


def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    value_1 = temperature
    value_2 = humidity
    value_3 = Temp

    # Creates a random gps coordinates
    lat = random.randrange(34, 36, 1) + \
        random.randrange(1, 1000, 1) / 1000.0
    lng = random.randrange(-83, -87, -1) + \
        random.randrange(1, 1000, 1) / 1000.0
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3}

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if _name_ == '_main_':
    while (True):
        main()
        time.sleep(1)
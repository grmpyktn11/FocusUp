import psutil
import time
import random
import http.client 
import urllib

from config import token, user
from phrases import phrases

amountOfTime = float(input("How often do you want to be reminded (in minutes)? "))


#post request
conn = http.client.HTTPSConnection("api.pushover.net:443")
def sendNotif():
    try:
        conn.request("POST", "/1/messages.json",
                      urllib.parse.urlencode({
                          "token": token,
                          "user": user,
                          "message": phrases[random.randint(0, len(phrases) - 1)],
                          "title": "FocusUp!"
                      }), {"Content-type": "application/x-www-form-urlencoded"})

        response = conn.getresponse()

        # Wait for the response before reading it
        while response.status == http.client.CONTINUE:
            response = conn.getresponse()

        # Check the response status
        if response.status == 200:
            print("Notification sent successfully.")
        else:
            print(f"Failed to send notification. Response status: {response.status}")
    except Exception as e:
        print(f"An error occurred during the HTTP request: {e}")
    finally:
        conn.close()

while True:
    vscIsRunning = ('Code.exe' in (i.name() for i in psutil.process_iter()) )
    if vscIsRunning:
        sendNotif()
    time.sleep(amountOfTime * 60)

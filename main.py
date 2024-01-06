import psutil
import time
import random
import http.client, urllib

from config import token, user
from phrases import phrases

amountOfTime = float(input("How often do you want to be reminded (in minutes)? "))


#post request
conn = http.client.HTTPSConnection("api.pushover.net:443")
def sendNotif():
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": token,
        "user": user,
        "message": phrases[random.randint(0,len(phrases) - 1)],
        "title": "FocusUp!"
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

vscIsRunning = ("Code.exe" in (i.name() for i in psutil.process_iter()) )

while True:
    vscIsRunning = ('Code.exe' in (i.name() for i in psutil.process_iter()) )
    if(vscIsRunning):
        sendNotif()
    time.sleep(amountOfTime*60)

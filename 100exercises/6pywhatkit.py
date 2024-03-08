import pywhatkit
from datetime import datetime

numCel = input("Cel: ")
message = input("Mensaje: ")
time = datetime.now().time()

#Send message to whatsapp
pywhatkit.sendwhatmsg(numCel, message, time.hour, time.minute+1)
pywhatkit.sendwhatmsg_instantly(numCel, message)


#Plays Lovely by billie ellish on youtube
pywhatkit.playonyt("lovely by billie")

#Take screenshot
pywhatkit.take_screenshot()
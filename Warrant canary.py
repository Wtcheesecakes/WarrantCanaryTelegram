import urllib.request
import time
while True:
    page = urllib.request.urlopen("https://api.azirevpn.com/v1/warrantcanary") #change this url to your canary
    content = str(page.read())
    if "Special note should be taken if this text is removed from this page" in content: #change this to the text on the page that you want to track
        print("All good")
        urllib.request.urlopen("https://api.telegram.org/botADDBOTAPIHERE/sendMessage?chat_id=@CHANNELNAME&text=All%20good") # add bot api and channel name
    else:
        urllib.request.urlopen("https://api.telegram.org/bot7ADDBOTAPIHERE/sendMessage?chat_id=@CHANNELNAME&text=Warrant%20canary%20missing") # add bot api and channel name
        print("Warrant canary missing")
    time.sleep(1800) #change this to the wait time you want 

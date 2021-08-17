import dotenv
from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message
import requests
from datetime import datetime
import schedule
import time
import csv

class MyPlugin(Plugin):
    def on_start(self):
        #Notifies general channel that the bot is now running.
        self.driver.create_post(channel_id=dotenv.get_key('.env', 'MAIN_CHANNEL_ID'), message="Je viens de me réveiller !")           
        self.scheduledMessages= self.getScheduledMessages()
        self.runScheduled()
                
    def on_stop(self):
        #Notifies general channel that the bot is shutting down.
        self.driver.create_post(channel_id=dotenv.get_key('.env', 'MAIN_CHANNEL_ID'), message="Je reviens ;)")
          
    ## actions from commands in user messages
    @listen_to("start", needs_mention=True)
    async def wake_up(self, message: Message):
        self.driver.reply_to(message, "Bonjour, Je suis Alfred, votre bot. Pour ceux qui ne me connaissent pas, je suis le majordome de grands hommes : Bruce Wayne (pas le charlatan de ce serveur, le vrai), Florian Forlini et Romain Manivel.")

    @listen_to("hey", needs_mention=True)
    async def hey(self, message: Message):
        self.driver.reply_to(message, "Moui, " + message.sender_name + " ?")

    @listen_to("meteo", needs_mention=True)
    async def weather(self, message: Message):
        submit = message.text.split(" ")
        answer = "Je n'ai rien trouvé."
        if (submit[0] == "meteo") :
            weather = await self.get_weather(submit[1], message)
            temp = weather['main']['temp']
            description = weather['weather'][0]['description']
            answer = message.sender_name + ", à " + submit[1] + ", il fait actuellement " + str(temp) + " degrés, et " + description + "."
        self.driver.reply_to(message, answer)

    async def get_weather(self, location, message: Message):
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&units=metric&lang=fr&appid=" + dotenv.get_key('.env', 'WEATHER_API')
        response = requests.get(api)
        return response.json()


    ## Scheduled messages from CSV file
    def runScheduled(self):
        for message in self.scheduledMessages:
            mday = message[0]
            mhour = message[1]
            mtext= message[2]
            setSchedule = 'schedule.every().' + mday + '.at("' + mhour + '").do(self.sendMessage, ("'+mtext+'"))'
            exec(setSchedule)


    def sendMessage(self, text):
        self.driver.create_post(channel_id=dotenv.get_key('.env', 'MAIN_CHANNEL_ID'), message=text)

    def getScheduledMessages(self):
        self.scheduledMessages = []
        with open("scheduledMessages.csv") as mess:
            messages = csv.reader(mess, delimiter= ";")
            for row in messages:
                days= row[0].split(',')
                for day in days:
                    day = self.findDay(day)
                    hours= row[1].split(',')
                    for hour in hours:
                        message=[day, hour, row[2]]
                        self.scheduledMessages.append(message)
                        
        return self.scheduledMessages
                    

    def findDay(self, dayNumber):
        days = ['monday', 'tuesday', 'wednesday', 'tuesday', 'friday', 'saturday', 'sunday']
        return days[int(dayNumber)]
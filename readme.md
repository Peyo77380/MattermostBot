# Alfred
## Python Bot for Mattermost
Periodiccaly send scheduled messages from CSV file.

## Requirement
### .env config
You need to add your settings in .env file. Weather API should be a OpenWeather Token

### Python Librairies
- dotenv : `pip install python-dotenv`
- mmpy_bot : `pip install -U mmpy_bot`
- schedule : `pip install schedule`
- requests : `pip install requests`
- datetime : `pip install DateTime`
- time : `pip install python-time`

### Change schedules messages
Everything is set in scheduledMessages.csv
Each row is a message, declared with :
dayNumbers;Hours;Message

Day numbers should be a list, each day is separated by a , 
0 = monday, 6 = sunday

Hours should be a list, each hour is separated by a ,
Each hours should have the format HH:MM or HH:MM:SS

Message is a string



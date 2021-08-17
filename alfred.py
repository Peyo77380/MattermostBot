#!/usr/bin/env python
import dotenv
from mmpy_bot import Bot, Settings
from my_plugin import MyPlugin

print(dotenv.dotenv_values('.env'))
bot = Bot(
    settings=Settings(
        MATTERMOST_URL = dotenv.get_key('.env', 'SERVER_URL'),
        MATTERMOST_PORT = int(dotenv.get_key('.env', 'SERVER_PORT')),
        BOT_TOKEN = dotenv.get_key('.env', 'BOT_TOKEN'),
        BOT_TEAM = dotenv.get_key('.env', 'BOT_TEAM'),
        SSL_VERIFY = True,
    ),  # Either specify your settings here or as environment variables.
    plugins=[MyPlugin()],  # Add your own plugins here.
)


bot.run()
import xmltodict
import requests
import discord
from discord.ext import commands
import asyncio
import threading
import time

#global configuration enviroment
lastUpdateId = 0000000000000000000000
filename = "video_id.txt"
token = "bot's token"
    
#video updates function
async def _lastVideo():
    xmlString = requests.get("https://youtube.com/feeds/videos.xml?channel_id=UCE2IvL50UAqkzCBKikDlClA")
    pythonDict=xmltodict.parse(xmlString.content)
    videoId = pythonDict.get("feed").get("entry")[0].get("yt:videoId")
    try:
        file = open(filename, 'r')
        line = file.readline()
        file.close()
        if line!=videoId:
            raise FileNotFoundError
    except FileNotFoundError:
        try:
            file = open(filename, "w")
            file.write(videoId)
            file.close()
            videoLink = "https://www.youtube.com/watch?v=" + videoId
            await bot.get_channel(lastUpdateId).send(f"{videoLink}\nHello @everyone,\nA new video is out on the channel, go quickly to see it I hope you enjoy it :)")
        except discord.errors.Forbidden:
            print("I've not enough permissions")
    await asyncio.sleep(60)
    await _lastVideo()

#bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
activity = discord.Activity(name="/help", type=discord.ActivityType.listening)
bot = commands.Bot(command_prefix="!",intents=intents, activity=activity)
bot.remove_command("help")

#discord events

#loading bot
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    #await bot.get_guild(guildId).get_channel(lastUpdateId).send(f"@everyone {_lastVideo()}")
    #await bot.get_all_channels()
    print("Logged as", bot.user)
    bot.loop.create_task(_lastVideo())

#run bot
bot.run(token)


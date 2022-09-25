import discord
from discord.ext import commands
from datetime import datetime as dt
from datetime import timedelta
import mysql.connector

#Globals variables and bot's options
hostname_db = "ip address"
username_db = "username"
password_db = "password"
guild_id = None #server_id
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
activity = discord.Activity(name="/help", type=discord.ActivityType.listening)
bot=commands.Bot(command_prefix="!",intents=intents, activity=activity)
bot.remove_command("help")

#custom function

#discord events
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("Logged as", bot.user)

@bot.event
async def on_message(message):
    user_id = message.author.id
    content = message.content
    channel = message.channel
    cur_time = dt.utcnow()
    cur_time_message = int(cur_time.strftime("%d%m%Y%H%M%S"))
    def spam_messages(mex):
        return mex.author == message.author and mex.content == message.content
    if message.author != bot.user and message.guild and message.guild.id == guild_id:
        try:
            conn = mysql.connector.Connect(host=hostname_db,user=username_db,password=password_db)
            cursor = conn.cursor()
            cursor.execute(f"SELECT last_message,flag FROM discord.spam WHERE user_id='{user_id}'")
            data = cursor.fetchall()
            if data:
                last_message,flag = data[0]
                #spam detected
                if cur_time_message-last_message>=0 and cur_time_message-last_message<=10:
                    if flag ==3:
                        cursor.execute(f"UPDATE discord.spam SET last_message={cur_time_message},flag=0 WHERE user_id='{user_id}'")
                        conn.commit()
                        await message.author.send(f"You've got over 3 spam warnings. You have been banned.")
                        await message.author.ban(reason="Over 3 spam warnings")
                    else:
                        cursor.execute(f"UPDATE discord.spam SET last_message={cur_time_message},flag={flag+1} WHERE user_id='{user_id}'")
                        conn.commit()
                        await message.author.timeout(cur_time + timedelta(minutes=5),reason="Spam")
                        await message.author.send(f"You're spamming. Every your message's going to be deleted. If you get over 3 warnings, you'll get banned.\nYour warnings: {flag+1}")
                        await channel.purge(check=spam_messages)
                #spam didn't detect
                else:
                    cursor.execute(f"UPDATE discord.spam SET last_message={cur_time_message} WHERE user_id='{user_id}'")
                    conn.commit()
            else:
                cursor.execute(f"INSERT INTO discord.spam (user_id,last_message) VALUES ('{user_id}',{cur_time_message})")
                conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.errors.Error:
            print("Database connection hasn't been established")
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Anything is wrong")

#Run the bot
bot.run("token-bot")
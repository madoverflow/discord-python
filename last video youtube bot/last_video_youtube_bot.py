
#global configuration enviroment
botId = "1004851812207177760"
lastUpdateId = "id of the channel for the last update"
guildId = "server id"
welcomeId = "welcome channel id"
goodbyeId = "goodbye channel id"
token = "bot token"
server = discord.utils.get(bot.guilds,id=int(guild_id))

#bot configuration
intents = discord.Intents.default()
intents.message_content = True
activity = discord.Activity(name="/help", type=discord.ActivityType.listening, buttons={"label1":"https//google.it"})
bot = commands.Bot(command_prefix="!",intents=intents, activity=activity)
bot.remove_command("help")


#discord events

#loading bot
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("Logged as", bot.user)
    #run periodic function to check new videos
    
#member join on server
@bot.event
async def on_member_join(member):
    if bot.user != member and server.get_channel(welcomeId):
        try:
            await bot.get_channel(welcome_id).send(f"@everyone {member.mention} "+welcome_message)
        except AttributeError:
            print("Channel's issue.")
        except discord.errors.Forbidden:
            print("Maybe, I'm not allowed to write on it.")
        except:
            print("Anything is wrong.")
            
#member left the server
@bot.event
async def on_member_remove(member):
    if bot.user != member and server.get_channel(goodbyeId):
        try:
            await bot.get_channel(goodbye_id).send(f"@everyone {member.mention} "+goodbye_message)
        except AttributeError:
            print("Channel's issue.")
        except discord.errors.Forbidden:
            print("Maybe, I'm not allowed to write on it.")
        except:
            print("Anything is wrong.")

#run bot
bot.run(token)

#server = discord.utils.get(bot.guilds,id=int(guild_id))
#        if server.get_channel(channel_id):


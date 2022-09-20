import discord
from discord.ext import commands

#Globals variables and bot's options
welcome_id = None #your channel id
welcome_message = None #welcome message
goodbye_message = None #goodbye message
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
activity = discord.Activity(name="/help", type=discord.ActivityType.listening)
bot=commands.Bot(command_prefix="!",intents=intents, activity=activity)
bot.remove_command("help")

#discord events
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("Logged as", bot.user)

@bot.event
async def on_member_join(member):
    if bot.user != member:
        try:
            await bot.get_channel(welcome_id).send(f"@everyone {member.mention} "+welcome_message)
        except AttributeError:
            print("Channel's issue.")
        except discord.errors.Forbidden:
            print("Maybe, I'm not allowed to write on it.")
        except:
            print("Anything is wrong.")

@bot.event
async def on_member_remove(member):
    if bot.user != member:
        try:
            await bot.get_channel(welcome_id).send(f"@everyone {member.mention} "+goodbye_message)
        except AttributeError:
            print("Channel's issue.")
        except discord.errors.Forbidden:
            print("Maybe, I'm not allowed to write on it.")
        except:
            print("Anything is wrong.")

#Run the bot
bot.run("token-bot")
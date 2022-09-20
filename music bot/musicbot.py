import discord
import youtube_dl
from discord.ext import commands
from discord import option
from discord import FFmpegPCMAudio

#Globals variables and bot's options
voice_channel = None
real_url = None
tile = None
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
activity = discord.Activity(name="/help", type=discord.ActivityType.listening)
bot=commands.Bot(command_prefix="!",intents=intents, activity=activity)
bot.remove_command("help")

#slash commands

@bot.slash_command(name="play",description="Play a song from youtube")
@option(
    name = "url",
    description = "Link youtube della canzone"
)
async def play(
    interaction : discord.Interaction,
    url : str):
    global voice_channel,real_url,title
    ydl_options = {'format': 'bestaudio', 'noplaylist':'True'}
    ffmepg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    ytd = youtube_dl.YoutubeDL(ydl_options)
    info = ytd.extract_info(url, download=False)
    url = info["url"]
    new_title = info["title"]
    channel = bot.get_channel(interaction.channel_id)
    try:
        voice_channel = await channel.connect()
        voice_channel.play(FFmpegPCMAudio(url, **ffmepg_options))
        await interaction.response.send_message(f"The bot is playing {new_title} in a few seconds.")
        real_url = url
        title = new_title
    except discord.errors.ClientException:
        print("The bot is already connected in the voice channel")
        if not voice_channel.is_playing():
            voice_channel.play(FFmpegPCMAudio(url, **ffmepg_options))
            await interaction.response.send_message(f"The bot is playing {new_title} in a few seconds.")
            real_url = url
            title = new_title
        else:
            await interaction.response.send_message(f"The bot hasn't finished to play the song {title}.")
    except AttributeError:
        await interaction.response.send_message("This is not a voice channel.")
    except:
        await interaction.response.send_message("Anything is wrong")

@bot.slash_command(name="stop",description="Stop the current song")
async def stop(interaction : discord.Interaction):
    if voice_channel:
        try:
            voice_channel.stop()
            await interaction.response.send_message("The song has correclty stopped.")
        except:
            await interaction.response.send_message("Anything is wrong. Maybe, the bot is playing no one song.")
    else:
        await interaction.response.send_message("The bot is no-one voice channel.")

@bot.slash_command(name="resume",description="Resume a song")
async def resume(interaction : discord.Interaction):
    if voice_channel and voice_channel.is_paused():
        try:
            voice_channel.resume()
            await interaction.response.send_message(f"You've resumed the song {title}.")
        except:
            await interaction.response.send_message("Anything is wrong. Maybe, the bot is playing no one song.")
    else:
        await interaction.response.send_message("The bot is either no-one voice channel or no one song is played.")

@bot.slash_command(name="pause",description="Pause the current song")
async def pause(interaction : discord.Interaction):
    if voice_channel:
        try:
            voice_channel.pause()
            await interaction.response.send_message("The song has correclty stopped.")
        except:
            await interaction.response.send_message("Anything is wrong. Maybe, the bot is playing no one song.")
    else:
        await interaction.response.send_message("The bot is no-one voice channel.")

@bot.slash_command(name="disconnect",description="Disconnect the bot from voice channel")
async def disconnect(interaction : discord.Interaction):
    try:
        await voice_channel.disconnect()
        await interaction.response.send_message("Bot disconnected.")
    except:
        await interaction.response.send_message("The bot is no-one voice channel.")

#discord events
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("Logged as", bot.user)

#Run the bot
bot.run("token-bot")
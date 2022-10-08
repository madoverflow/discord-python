from dataclasses import field
import discord
import time
from discord.ext import commands
from discord import option
from datetime import datetime as dt
from datetime import timedelta
import mysql.connector

#Globals variables and bot's options
hostname_db = "id"
username_db = "username"
password_db = "password"
guild_id = None #server id
log_id = None #log channel id
welcome_id = None #welcome channel id
goodbye_id = None #goodbye channel id
welcome_message = "welcome to our awesome server."
goodbye_message = "bye my friend. See you later."
admin_list = ["admin_id","etc..."]
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True
intents.guilds = True
intents.presences = True
activity = discord.Activity(name="/help", type=discord.ActivityType.listening)
bot=commands.Bot(command_prefix="!",intents=intents, activity=activity)
bot.remove_command("help")

#custom function
def perm(b,a):
    fb = ""
    fa = ""
    if b.add_reactions != a.add_reactions:
        fb = fb + f"`Add reactions`: {b.add_reactions}\n"
        fa = fa + f"`Add reactions`: {a.add_reactions}\n"
    if b.administrator != a.administrator:
        fb = fb + f"`Administrator`: {b.administrator}\n"
        fa = fa + f"`Administrator`: {a.administrator}\n"
    if b.attach_files != a.attach_files:
        fb = fb + f"`Attach Files`: {b.attach_files}\n"
        fa = fa + f"`Attach Files`: {a.attach_files}\n"
    if b.ban_members != a.ban_members:
        fb = fb + f"`Ban Members`: {b.ban_members}\n"
        fa = fa + f"`Ban Members`: {a.ban_members}\n"
    if b.change_nickname != a.change_nickname:
        fb = fb + f"`Change Nickname`: {b.change_nickname}\n"
        fa = fa + f"`Change Nickname`: {a.change_nickname}\n"
    if b.connect != a.connect:
        fb = fb + f"`Connect`: {b.connect}\n"
        fa = fa + f"`Connect`: {a.connect}\n"
    if b.create_instant_invite != a.create_instant_invite:
        fb = fb + f"`Create Instant Invite`: {b.create_instant_invite}\n"
        fa = fa + f"`Create Instant Invite`: {a.create_instant_invite}\n"
    if b.create_private_threads != a.create_private_threads:
        fb = fb + f"`Create Private Threads`: {b.create_private_threads}\n"
        fa = fa + f"`Create Private Threads`: {a.create_private_threads}\n"
    if b.create_public_threads != a.create_public_threads:
        fb = fb + f"`Create Public Threads`: {b.create_public_threads}\n"
        fa = fa + f"`Create Public Threads`: {a.create_public_threads}\n"
    if b.deafen_members != a.deafen_members:
        fb = fb + f"`Deafen Members`: {b.deafen_members}\n"
        fa = fa + f"`Deafen Members`: {a.deafen_members}\n"
    if b.embed_links != a.embed_links:
        fb = fb + f"`Embed Links`: {b.embed_links}\n"
        fa = fa + f"`Embed Links`: {a.embed_links}\n"
    if b.external_emojis != a.external_emojis:
        fb = fb + f"`External Emojis`: {b.external_emojis}\n"
        fa = fa + f"`External Emojis`: {a.external_emojis}\n"
    if b.external_stickers != a.external_stickers:
        fb = fb + f"`External Stickers`: {b.external_stickers}\n"
        fa = fa + f"`External Stickers`: {a.external_stickers}\n"
    if b.kick_members != a.kick_members:
        fb = fb + f"`Kick Members`: {b.kick_members}\n"
        fa = fa + f"`Kick Members`: {a.kick_members}\n"
    if b.manage_channels != a.manage_channels:
        fb = fb + f"`Manage Channels`: {b.manage_channels}\n"
        fa = fa + f"`Manage Channels`: {a.manage_channels}\n"
    if b.manage_emojis != a.manage_emojis:
        fb = fb + f"`Manage Emojis`: {b.manage_emojis}\n"
        fa = fa + f"`Manage Emojis`: {a.manage_emojis}\n"
    if b.manage_emojis_and_stickers != a.manage_emojis_and_stickers:
        fb = fb + f"`Manage Emojis and Stickers`: {b.manage_emojis_and_stickers}\n"
        fa = fa + f"`Manage Emojis and Stickersr`: {a.manage_emojis_and_stickers}\n"
    if b.manage_events != a.manage_events:
        fb = fb + f"`Manage Events`: {b.manage_events}\n"
        fa = fa + f"`Manage Events`: {a.manage_events}\n"
    if b.manage_guild != a.manage_guild:
        fb = fb + f"`Manage Guild`: {b.manage_guild}\n"
        fa = fa + f"`Manage Guild`: {a.manage_guild}\n"
    if b.manage_messages != a.manage_messages:
        fb = fb + f"`Manage Messages`: {b.manage_messages}\n"
        fa = fa + f"`Manage Messages`: {a.manage_messages}\n"
    if b.manage_nicknames != a.manage_nicknames:
        fb = fb + f"`Manage Nicknames`: {b.manage_nicknames}\n"
        fa = fa + f"`Manage Nicknames`: {a.manage_nicknames}\n"
    if b.manage_permissions != a.manage_permissions:
        fb = fb + f"`Manage Permissions`: {b.manage_permissions}\n"
        fa = fa + f"`Manage Permissions`: {a.manage_permissions}\n"
    if b.manage_roles != a.manage_roles:
        fb = fb + f"`Manage Roles`: {b.manage_roles}\n"
        fa = fa + f"`Manage Roles`: {a.manage_roles}\n"
    if b.manage_threads != a.manage_threads:
        fb = fb + f"`Manage Threads`: {b.manage_threads}\n"
        fa = fa + f"`Manage Threads`: {a.manage_threads}\n"
    if b.manage_webhooks != a.manage_webhooks:
        fb = fb + f"`Manage Webhooks`: {b.manage_webhooks}\n"
        fa = fa + f"`Manage Webhooks`: {a.manage_webhooks}\n"
    if b.mention_everyone!= a.mention_everyone:
        fb = fb + f"`Mention Everyone`: {b.mention_everyone}\n"
        fa = fa + f"`Mention Everyone`: {a.amention_everyone}\n"
    if b.moderate_members != a.moderate_members:
        fb = fb + f"`Moderate Members`: {b.amoderate_members}\n"
        fa = fa + f"`Moderate Members`: {a.moderate_members}\n"
    if b.move_members != a.move_members:
        fb = fb + f"`Move Members`: {b.move_members}\n"
        fa = fa + f"`Move Members`: {a.move_members}\n"
    if b.mute_members != a.mute_members:
        fb = fb + f"`Mute Members`: {b.mute_members}\n"
        fa = fa + f"`Mute Members`: {a.mute_members}\n"
    if b.priority_speaker != a.priority_speaker:
        fb = fb + f"`Priority Speaker`: {b.priority_speaker}\n"
        fa = fa + f"`Priority Speaker`: {a.priority_speaker}\n"
    if b.read_message_history != a.read_message_history:
        fb = fb + f"`Read Message History`: {b.read_message_history}\n"
        fa = fa + f"`Read Message History`: {a.read_message_history}\n"
    if b.read_messages != a.read_messages:
        fb = fb + f"`Read Messages`: {b.read_messages}\n"
        fa = fa + f"`Read Messages`: {a.read_messages}\n"
    if b.request_to_speak != a.request_to_speak:
        fb = fb + f"`Request to Speak`: {b.request_to_speak}\n"
        fa = fa + f"`Request to Speak`: {a.request_to_speak}\n"
    if b.send_messages != a.send_messages:
        fb = fb + f"`Send Messages`: {b.send_messages}\n"
        fa = fa + f"`Send Messages`: {a.send_messages}\n"
    if b.send_messages_in_threads != a.send_messages_in_threads:
        fb = fb + f"`Send Messages in Threads`: {b.send_messages_in_threads}\n"
        fa = fa + f"`Send Messages in Threads`: {a.send_messages_in_threads}\n"
    if b.send_tts_messages != a.send_tts_messages:
        fb = fb + f"`Send tts Messages`: {b.send_tts_messages}\n"
        fa = fa + f"`Send tts Messages`: {a.send_tts_messages}\n"
    if b.speak != a.speak:
        fb = fb + f"`Speak`: {b.speak}\n"
        fa = fa + f"`Speak`: {a.speak}\n"
    if b.stream != a.stream:
        fb = fb + f"`Stream`: {b.stream}\n"
        fa = fa + f"`Stream`: {a.stream}\n"
    if b.use_application_commands != a.use_application_commands:
        fb = fb + f"`Use Application Commands`: {b.use_application_commands}\n"
        fa = fa + f"`Use Application Commands`: {a.use_application_commands}\n"
    if b.use_external_emojis != a.use_external_emojis:
        fb = fb + f"`Use External Emojis`: {b.use_external_emojis}\n"
        fa = fa + f"`Use External Emojis`: {a.use_external_emojis}\n"
    if b.use_external_stickers != a.use_external_stickers:
        fb = fb + f"`Use External Stickers`: {b.use_external_stickers}\n"
        fa = fa + f"`Use External Stickers`: {a.use_external_stickers}\n"
    if b.use_voice_activation != a.use_voice_activation:
        fb = fb + f"`Use Voice Activation`: {b.use_voice_activation}\n"
        fa = fa + f"`Use Voice Activation`: {a.use_voice_activation}\n"
    if b.value != a.value:
        fb = fb + f"`Value`: {b.value}\n"
        fa = fa + f"`Value`: {a.value}\n"
    if b.view_audit_log != a.view_audit_log:
        fb = fb + f"`View audit Log`: {b.view_audit_log}\n"
        fa = fa + f"`View audit Log`: {a.view_audit_log}\n"
    if b.view_channel != a.view_channel:
        fb = fb + f"`View Channel`: {b.view_channel}\n"
        fa = fa + f"`View Channel`: {a.view_channel}\n"
    if b.view_guild_insights != a.view_guild_insights:
        fb = fb + f"`View Guild Insights`: {b.view_guild_insights}\n"
        fa = fa + f"`View Guild Insights`: {a.view_guild_insights}\n"
    if not fb:
        fb = "Nothing is changed"
    if not fa:
        fa = "Nothing is changed"
    return (fb,fa)

#slash commands
@bot.slash_command(name="purge", description="Delete messages of a channel", guild_only=guild_id)
@option(
    name = "channel_id",
    description = "Channel id"
)
@option(
    name = "limit",
    description = "Messages number to check or delete"
)
@option(
    name = "user_id",
    description = "Id of the messages' author"
)
async def purge(
    interaction : discord.Interaction, 
    channel_id : str, 
    limit=None, 
    user_id=None):
    membri = bot.get_all_members()
    def is_member(messaggio):
        return utente == None or messaggio.author.id == utente.id 
    if interaction.user.id in admin_list: 
        try:
            channel_id = int(channel_id)
            if limit != None:
                limit = int(limit)
            if user_id != None:
                user_id = int(user_id)
            channel = bot.get_channel(channel_id)
            utente = discord.utils.get(membri,id=user_id)
            await channel.send("@everyone Warning: some messages will be deleted in a few minutes.")
            await interaction.response.send_message("Cleaning correctly started.",ephemeral=True)
            time.sleep(10)
            await channel.purge(limit=limit, check=is_member)
            await interaction.channel.send(f"<@{interaction.user.id}> Cleaning completed.")
        except AttributeError:
            await interaction.response.send_message("Channel id is wrong.\nTry again.",ephemeral=True)
        except ValueError:
            await interaction.response.send_message("Data format is wrong.\nTry again.",ephemeral=True)
        except discord.errors.Forbidden:
            await interaction.response.send_message("Missing permission to clean the channel.",ephemeral=True)
        except:
            await interaction.response.send_message("Something is wrong.\n Check data you sent.",ephemeral=True)
    else:
        await interaction.response.send_message("You're not allowed to run this command.\nYou're not fun.",ephemeral=True)

#discord events
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print("Logged as", bot.user)

@bot.event
async def on_message(message):
    user_id = message.author.id
    channel = message.channel
    ghost_message = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||"
    cur_time = dt.utcnow()
    cur_time_message = int(cur_time.strftime("%d%m%Y%H%M%S"))
    color = 0x6358f3
    field_id = f"""🙍‍♂️ `user`: {message.author.id}
    📃 `message`: {message.id}
    📢 `channel`: {message.channel.id}"""
    channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
    def spam_messages(mex):
        return mex.author == message.author and mex.content == message.content
    if message.author != bot.user and message.guild and message.guild.id == guild_id:
        #ghost ping detected
        if ghost_message in message.content:
            await message.author.send(f"Ghost ping is not allowed. You have been banned.")
            await message.author.ban(reason="Ghost ping")
            description = f"Ghost ping detected inside a message on channel {message.channel.mention}\nThe user has been banned."
            channel_message = discord.Embed(description=description,color=color)
            channel_message.set_thumbnail(url="https://bot.to/wp-content/uploads/2020/10/anti-ghost-ping_5f7e1433e80c3.png")
            channel_message.set_author(name=message.author,icon_url=message.author.display_avatar)
            channel_message.add_field(name="ID",value=field_id,inline=False)
            try:
                await channel_log.send(embed=channel_message)
            except discord.errors.Forbidden:
                print("Missing permissions.")
            except:
                print("Something is wrong.")
        #ghost ping didn't detect
        else:
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
                            description = f"The user has been banned because it gets over 3 warnings for spamming."
                            channel_message = discord.Embed(description=description,color=color)
                        else:
                            cursor.execute(f"UPDATE discord.spam SET last_message={cur_time_message},flag={flag+1} WHERE user_id='{user_id}'")
                            conn.commit()
                            await message.author.timeout(cur_time + timedelta(minutes=5),reason="Spam")
                            await message.author.send(f"You're spamming. Every your message's going to be deleted. If you get over 3 warnings, you'll get banned.\nYour warnings: {flag+1}")
                            await channel.purge(check=spam_messages)
                            description = f"The user has been spamming. It has got a timeout of 5 minutes\n⚠Total warnings: {flag+1}."
                            channel_message = discord.Embed(description=description,color=color)
                        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
                        channel_message.set_author(name=message.author,icon_url=message.author.display_avatar)
                        channel_message.add_field(name="ID",value=field_id,inline=False)
                        try:
                            await channel_log.send(embed=channel_message)
                        except discord.errors.Forbidden:
                            print("Missing permissions.")
                        except:
                            print("Something is wrong.")
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
                print("Something is wrong")

@bot.event
async def on_message_delete(message):
    if message.guild and message.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        field_id = f"""🙍‍♂️ `user`: {message.author.id}
        📃 `message`: {message.id}
        📢 `channel`: {message.channel.id}"""
        #ghost ping detected
        if message.mentions or message.role_mentions or message.mention_everyone:
            description = f"Possible ghost ping detected on channel {message.channel.mention}"
            color = 0x6358f3
            channel_message = discord.Embed(description=description,color=color)
            channel_message.set_thumbnail(url="https://bot.to/wp-content/uploads/2020/10/anti-ghost-ping_5f7e1433e80c3.png")
        #ghost ping didn't detect
        else:
            description = f"Message deleted on channel {message.channel.mention}"
            color = 0x8e8e8e
            channel_message = discord.Embed(description=description,color=color)
            channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=message.author,icon_url=message.author.display_avatar)
        channel_message.add_field(name="Content",value=message.content,inline=False)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_message_edit(before,after):
    if before.guild and before.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        field_id = f"""🙍‍♂️ `user`: {before.author.id}
        📃 `message`: {before.id}
        📢 `channel`: {before.channel.id}"""
        #ghost ping detected
        if before.mentions or before.role_mentions or before.mention_everyone:
            description = f"Possible ghost ping detected on channel {before.channel.mention}"
            color = 0x6358f3
            channel_message = discord.Embed(description=description,color=color)
            channel_message.set_thumbnail(url="https://bot.to/wp-content/uploads/2020/10/anti-ghost-ping_5f7e1433e80c3.png")
        #ghost ping didn't detect
        else:
            description = f"Message edited on channel {before.channel.mention}"
            color = 0x8e8e8e
            channel_message = discord.Embed(description=description,color=color)
            channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=before.author,icon_url=before.author.display_avatar)
        channel_message.add_field(name="Before editing",value=before.content,inline=False)
        channel_message.add_field(name="After editing",value=after.content,inline=False)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_guild_channel_create(channel):
    if channel.guild and channel.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        roles = channel.changed_roles
        description = f"New channel was created {channel.mention}"
        color = 0x8e8e8e
        field_id = f"📢 `channel`: {channel.id}"
        list_roles = ""
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=channel.category.name,icon_url=channel.guild.icon)
        if roles:
            for rol in roles:
                list_roles = list_roles + f"{rol.mention}\n"
            channel_message.add_field(name="Roles list",value=list_roles,inline=False)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_guild_channel_delete(channel):
    if channel.guild and channel.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        description = f"{channel.name.capitalize()} was deleted"
        color = 0x8e8e8e
        field_id = f"📢 `channel`: {channel.id}"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=channel.category.name,icon_url=channel.guild.icon)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_guild_channel_update(before, after):
    if before.guild and before.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        after_roles = after.changed_roles
        description = f"{before.mention} was edited"
        color = 0x8e8e8e
        field_id = f"📢 `channel`: {before.id}"
        before_edit = f"Name: {before.name}\nMention: {before.mention}\nPosition: {before.position}\n"
        after_edit = f"Name: {after.name}\nMention: {after.mention}\nPosition: {after.position}\n"
        roles = "Empty"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=before.category.name,icon_url=before.guild.icon)
        if after_roles:
            roles = ""
            for rol in after_roles:
                roles = roles + f"{rol.mention}\n"
        channel_message.add_field(name="Before editing",value=before_edit,inline=True)
        channel_message.add_field(name="After editing",value=after_edit,inline=True)
        channel_message.add_field(name="🔑Roles list",value=roles,inline=False)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_guild_role_delete(role):
    if role.guild and role.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        description = f"{role.name.capitalize()} was deleted"
        color = 0x8e8e8e
        field_config = f"""Position: {role.position}
        Mentionable: {role.mentionable}
        Displayed separately from other members: {role.hoist}"""
        field_id = f"🛂 `role`: {role.id}"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name="Role event",icon_url=role.guild.icon)
        channel_message.add_field(name="Config list",value=field_config,inline=False)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_guild_role_update(before, after):
    if before.guild and before.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        after_members = after.members
        before_permissions = before.permissions
        after_permissions = after.permissions
        field_before_config = f"""Name: {before.name}
        Position: {before.position}
        Mentionable: {before.mentionable}
        Displayed separately from other members: {before.hoist}"""
        field_after_config = f"""Name: {after.name}
        Position: {after.position}
        Mentionable: {after.mentionable}
        Displayed separately from other members: {after.hoist}"""
        field_id = f"🛂 `role`: {before.id}"
        if after_members:
            field_after_members = ""
            for member in after_members:
                field_after_members = field_after_members + f"{member.mention}\n"
        else:
            field_after_members = "Empty"
        field_before_permissions,field_after_permissions = perm(before_permissions,after_permissions)
        description = f"{before.mention} was edited"
        color = 0x8e8e8e
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_author(name="Role event",icon_url=before.guild.icon)
        channel_message.add_field(name="Config Pre-Edit",value=field_before_config,inline=True)
        channel_message.add_field(name="Config Post-Edit",value=field_after_config,inline=True)
        channel_message.add_field(name="Members list",value=field_after_members,inline=False)
        channel_message.add_field(name="Permissions Pre-Edit",value=field_before_permissions,inline=True)
        channel_message.add_field(name="Permissions Post-Edit",value=field_after_permissions,inline=True)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_thread_create(thread):
    if thread.guild and thread.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        description = f"New thread was created {thread.mention} on channel {thread.parent.mention}"
        color = 0x8e8e8e
        field_id = f"📢 `thread`: {thread.id}"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=f"{thread.category.name}/{thread.parent.name}",icon_url=thread.guild.icon)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_thread_delete(thread):
    if thread.guild and thread.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        description = f"Thread `{thread.name}` was deleted on channel {thread.parent.mention}"
        color = 0x8e8e8e
        field_id = f"📢 `thread`: {thread.id}"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=f"{thread.category.name}/{thread.parent.name}",icon_url=thread.guild.icon)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

@bot.event
async def on_thread_update(before, after):
    if before.guild and before.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        description = f"{before.mention} was edited"
        color = 0x8e8e8e
        field_id = f"📢 `thread`: {before.id}"
        before_edit = f"Name: {before.name}\nMention: {before.mention}\nParent: {before.parent.mention}\n"
        after_edit = f"Name: {after.name}\nMention: {after.mention}\nParent: {after.parent.mention}\n"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/computer-programming-dazzle-vol-2/256/Logs-512.png")
        channel_message.set_author(name=f"{before.category.name}/{before.parent.name}",icon_url=before.guild.icon)
        channel_message.add_field(name="Before editing",value=before_edit,inline=True)
        channel_message.add_field(name="After editing",value=after_edit,inline=True)
        channel_message.add_field(name="ID",value=field_id,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

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
            await bot.get_channel(goodbye_id).send(f"@everyone {member.mention} "+goodbye_message)
        except AttributeError:
            print("Channel's issue.")
        except discord.errors.Forbidden:
            print("Maybe, I'm not allowed to write on it.")
        except:
            print("Anything is wrong.")

@bot.event
async def on_member_update(before,after):
    if before.guild and before.guild.id == guild_id:
        channel_log = discord.utils.get(bot.get_all_channels(),id=log_id)
        description = f"{after} changed its profile"
        field_info = f"""🙍‍♂️ `user`: {after.id}
        `🔰username`: {after.name}
        `📛username#tag`: {after}
        `⭕status`: {after.status}
        `🤖bot user`: {after.bot}
        `🛡 system user`: {after.system}"""
        field_before = f"""`Nickname`: {before.nick}
        `Roles list`:\n"""
        field_after = f"""`Nickname`: {after.nick}
        `Roles list`:\n"""
        color = 0x8e8e8e
        before_roles = before.roles
        after_roles = after.roles
        for role in before_roles:
            field_before = field_before + f"{role.mention}\n"
        for role in after_roles:
            field_after = field_after + f"{role.mention}\n"
        channel_message = discord.Embed(description=description,color=color)
        channel_message.set_author(name=after,icon_url=before.display_avatar)
        channel_message.add_field(name="Before editing",value=field_before,inline=False)
        channel_message.add_field(name="After editing",value=field_after,inline=False)
        channel_message.add_field(name="ID",value=field_info,inline=False)
        try:
            await channel_log.send(embed=channel_message)
        except discord.errors.Forbidden:
            print("Missing permissions.")
        except:
            print("Something is wrong.")

#Run the bot
bot.run("token-bot")
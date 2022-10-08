
![Logo](https://i.postimg.cc/WbY6fhmm/security-bot.png)


# Security Bot

Best security bot with premium functions. What can it do? 

## Skills ⚔

- ### Welcome/goodbye bot: 
  Set a custom message when a user joins into your discord server or the user leaves it.
- ### Antispam bot: 
  It will mute a user for spamming. After 3 warnings, it will get banned.
  The spam is caught if the second difference between two messages is under 10 seconds.
- ### Anti ghost ping:
  Ghost ping is caught with text bugged, user mention and deleting message.
- ### Log bot:
  Every discord stranger thing/update will be reported in a server log channel.
- ### Clean:
  Use the purge command to clean a server channel.

## Commands

- #### Purge

    | Parameter | Type     | Description                |
    | :-------- | :------- | :------------------------- |
    | `channel_id` | `int` | **Required**. Id channel |
    | `limit` | `int` | **Optional**. Number message to delete. **Default/max** value: 100 |
    | `user_id` | `int` | **Option**. Messaged sender id  |



## Installation

You must install the follow modules to run this script:

```bash
  pip install -U discord
  pip install py-cord
  pip install mysql-connector-python
```
Import database and table from file `database.sql`.
    
## Globals Variables

This Python script uses the follow globals variables

`hostname_db`: mysql server address

`username_db`: mysql account username

`password_db`: mysql account password

`guild_id`: server id

`log_id`: log channel id

`welcome_id`: welcome channel id

`goodbye_id`: goodbye channel id

`welcome_message`: custom welcome message

`goodbye_message`: cutsom goodbye message

`admin_list`: list of admins' id

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.txt)


## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![Python](https://img.shields.io/pypi/pyversions/django)](https://www.python.org/)


## Documentation

[Api discord reference](https://discordpy.readthedocs.io/)

[Api py-cord reference](https://docs.pycord.dev/)
 
[Mysql reference](https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html)

# Hi, I'm Emanuele! 👋

I'm a computer science student in [UNIPA](https://www.unipa.it/)
## 🔗 Links
[![telegram](https://img.shields.io/static/v1?label=Telegram&message=Link&color=blue)](https://t.me/emanuelecastronovo)
[![discord](https://img.shields.io/static/v1?label=Discord&message=@madoverflow9116&color=blueviolet)](https://discord.com/)

## 🖥 Known programming languages
C, Java, Python, PHP


## Support

You can send me a message on [Telegram](https://t.me/emanuelecastronovo) or discord.




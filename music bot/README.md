
![Logo](https://i.postimg.cc/9MGW5csC/1-pg-Oj-BS0d-mc10-JJG8y-KGv-Q.png)


# Music Bot

A simble bot to play every youtube song.


## Commands

- #### Play: play a song

    | Parameter | Type     | Description                |
    | :-------- | :------- | :------------------------- |
    | `url` | `string` | **Required**. Youtube song link |

- #### Pause: pause the current song

- #### Resume: resume last paused song

- #### Stop: stop the play song. It won't can be resumed

- #### Disconnect: disconnect the bot from voice channel



## Installation

You must install the follow modules to run this script:

```bash
  pip install -U discord
  pip install py-cord
  pip install youtube-dl
```
Install ffmpeg. For windows, you can see this [video](https://www.youtube.com/watch?v=a_KqycyErd8)
    
## Globals Variables

This Python script uses the follow globals variables

`voice_channel`

`real_url`

`title`

`bot`


## Usage/Examples

You can **ONLY** play a song inside a voice channel.

When you play a song in a voice channel and you want change the voice channel,
you must disconnect the bot from the voice channel. You can do it with the slash command `/disconnect`.
For example:

```python
#user log-in voice channel 1
/play url:link_youtube

#user log-in voice channel 2. Correct way to play a song:
/disconnect
/play url:link_youtube

#user log-in voice channel 2. Wrong way to play a song:
/play url:link_youtube
#the bot will play the song inside the voice channel 1.
```


## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.txt)


## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![Python](https://img.shields.io/pypi/pyversions/django)](https://www.python.org/)


## Documentation

[Api discord reference](https://discordpy.readthedocs.io/)

[Api py-cord reference](https://docs.pycord.dev/)

[Youtube-dl reference](https://github.com/ytdl-org/youtube-dl/tree/3e4cedf9e8cd3157df2457df7274d0c842421945)
 
[FFMPEG](https://ffmpeg.org/)

# Hi, I'm Emanuele! 👋

I'm a computer science student in [UNIPA](https://www.unipa.it/)
## 🔗 Links
[![telegram](https://img.shields.io/static/v1?label=Telegram&message=Link&color=blue)](https://t.me/emanuelecastronovo)
[![discord](https://img.shields.io/static/v1?label=Discord&message=@madoverflow9116&color=blueviolet)](https://discord.com/)

## 🖥 Known programming languages
C, Java, Python, PHP


## Support

You can send me a message on [Telegram](https://t.me/emanuelecastronovo) or discord.


# Lilliebot

Lilliebot is a discord bot that can post a range of pokemon information, from base stats to just simply a picture. 

Things to know to get Lilliebot to run
Python 3.x is required to run the bot.

Next Lilliebot has 2 dependencies
First is discord.py which full installation instructions can be found here
https://github.com/Rapptz/discord.py
But all that is needed can be installed by running
```
python3 -m pip install -U discord.py
```

Second is requests which can be installed by running
```
python3 -m pip install -U requests
```

In order to run the bot you need to create a Discord application here

https://discordapp.com/developers/applications/me

Give the app a name and then turn it into a bot user.

Once that is done get the App Bot User Token, create a text file named token.txt and put your token in it.

To invite the bot to your server replace bot-id in the following URL with your bot's specific client ID,
which is also found on the applications page. 

Invite URL: https://discordapp.com/oauth2/authorize?client_id=bot-id&scope=bot&permissions=0

After adding the bot to your server you can run it by typing: 

"python3 lilliebot.py"

In a terminal from the directory that lilliebot was put in.

Once running you can type \*help in a text channel to get a list and description of all of Lilliebots commands

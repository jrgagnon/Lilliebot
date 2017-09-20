import discord
import asyncio
from lb_functions import help, stats, format

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # Info
    if message.content.startswith('*info'):
        m = '```Hello, I am Lillie\n' \
            + 'Type *help for a list of commands```'
        await client.send_message(message.channel, m)

    # Pic
    elif message.content.startswith('*pic'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:

            if args[1].isnumeric():
                info = stats(1, args[1])
            else:
                info = stats(2, args[1])

            m = info[0]

            await client.send_message(message.channel, m)

    # Stats
    elif message.content.startswith('*stats'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:

            if args[1].isnumeric():
                info = stats(1, args[1])
            else:
                info = stats(2, args[1])


            m = format(info)
            await client.send_message(message.channel, info[0])
            await client.send_message(message.channel, m)

    # Help
    elif message.content.startswith('*help'):
        await client.send_message(message.channel, help())

# Put bot token here
bot_token = 

client.run(bot_token)

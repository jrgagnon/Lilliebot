import discord
import asyncio
import requests
import io
import os
from lb_pokemon import stats, mega
from lb_functions import types, dual_types, mono, ability, nature
from lb_moves import move_info, move_print
from lb_utilities import get_token, stats_print, types_print, mega_print, ability_print, help, nature_print
from lb_typeing import Type, generate_type_table, generate_effectiveness, print_effectiveness


client = discord.Client()

type_table = generate_type_table()
e = generate_effectiveness(type_table, 'Fire', 'Flying')
# 2x Weak e[0] ^ e[1]
# 4x Weak e[0] & e[1]
# 1/2 resistant e[2] ^ e[3]
# 1/4 resistant e[2] & e[3]
# immune e[4] ^ e[5]
m = print_effectiveness(e)
print(m)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    game = discord.Game(name=u'Get in the Bag Nebby')
    await client.change_presence(game=game)


@client.event
async def on_message(message):
    # Info
    if message.content.startswith('*info'):
        m = '```Hello, I am Lillie\n' \
            + 'Type *help for a list of commands```'
        await client.send_message(message.channel, m)

        game = discord.Game(name=u'Get in the Bag Nebby')
        await client.change_presence(game=game)

    # Pic
    elif message.content.startswith('*pic'):
        args = message.content.upper().split()

        #arguments will be less than 2 if no number or name is given
        if len(args) < 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')

        #arguments equal to 3 means that the passed pokemon has a two word name
        elif len(args) == 3:

            #combine the 2 words to make 1 string
            pkmn_name = args[1] + ' ' + args[2]
            info = stats(2, pkmn_name)

        #single word name or number is given
        else:

            #check to see if a number is passed
            if args[1].isnumeric():
                info = stats(1, args[1])
            else:
                info = stats(2, args[1])

        if info != -1:
            #Download Image to temp and Post
            r = requests.get(info[0], stream=True)
            img = io.BytesIO(r.content)

            temporarylocation="pokemon.png"
            with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
                out.write(img.read())                ## Read bytes into file

            await client.send_file(message.channel, temporarylocation)
            os.remove(temporarylocation) ## Delete file when done

    # Stats
    elif message.content.startswith('*stats'):
        args = message.content.upper().split()

        #arguments will be less than 2 if no number or name is given
        if len(args) < 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')

        #arguments equal to 3 means that the passed pokemon has a two word name
        elif len(args) == 3:

            #combine the 2 words to make 1 string
            pkmn_name = args[1] + ' ' + args[2]
            info = stats(2, pkmn_name)

        #single word name or number is given
        else:

            #check to see if a number is passed
            temp = args[1][0:-1]
            if args[1].isnumeric():
                info = stats(1, args[1])
            elif temp.isnumeric():
                info = stats(1, args[1])
            else:
                info = stats(2, args[1])

        if info != -1:
            m = stats_print(info)

            #Download Image to temp and Post
            r = requests.get(info[0], stream=True)
            img = io.BytesIO(r.content)
            temporarylocation="pokemon.png"
            with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
                out.write(img.read())                ## Read bytes into file

            await client.send_file(message.channel, temporarylocation)
            os.remove(temporarylocation) ## Delete file when done

            await client.send_message(message.channel, m)

    # Mega
    elif message.content.startswith('*mega'):
        args = message.content.upper().split()

        #arguments will be less than 2 if no number or name is given
        if len(args) < 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')

        #arguments equal to 3 means that the passed pokemon has a two word name
        elif len(args) == 3:

            #combine the 2 words to make 1 string
            pkmn_name = args[1] + ' ' + args[2]
            info = stats(2, pkmn_name)

        #single word name or number is given
        else:

            temp = args[1][0:-1]
            if args[1].isnumeric():
                info = mega(1, args[1])
            elif temp.isnumeric():
                info = mega(1, args[1])
            else:
                info = mega(2, args[1])

        if info != -1:
            m = mega_print(info)

            #Download Image to temp and Post
            r = requests.get(info[0], stream=True)
            img = io.BytesIO(r.content)

            temporarylocation="pokemon.png"
            with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
                out.write(img.read())                ## Read bytes into file

            await client.send_file(message.channel, temporarylocation)
            os.remove(temporarylocation) ## Delete file when done

            await client.send_message(message.channel, m)

    # Move
    elif message.content.startswith('*move'):
        args = message.content.upper().split()
        if len(args) < 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        elif len(args) == 3:

            move_name = args[1] + ' ' + args[2]
            info = move_info(move_name)

            if info != -1:
                m = move_print(info)
                await client.send_message(message.channel, m)
        else:
            info = move_info(args[1])

            if info != -1:
                m = move_print(info)
                await client.send_message(message.channel, m)

    # Help
    elif message.content.startswith('*help'):
        await client.send_message(message.channel, help())

    # Type
    elif message.content.startswith('*type'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            type_list = types(args[1])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))

    # Dual
    elif message.content.startswith('*dual'):
        args = message.content.upper().split()
        if len(args) != 3:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            type_list = dual_types(args[1], args[2])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))

    # Mono
    elif message.content.startswith('*mono'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            type_list = mono(args[1])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))

    # Ability
    elif message.content.startswith('*ability'):
        args = message.content.upper().split()
        if len(args) < 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        elif len(args) == 3:

            ability_name = args[1] + ' ' + args[2]
            info = ability(ability_name)

            if info != -1:
                m = ability_print(info)
                await client.send_message(message.channel, m)
        else:
            info = ability(args[1])

            if info != -1:
                m = ability_print(info)
                await client.send_message(message.channel, m)

    # nature
    elif message.content.startswith('*nature'):
        args = message.content.upper().split()
        if len(args) != 2:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            info = nature(args[1])
            if info != -1:
                m = nature_print(info)
                await client.send_message(message.channel, m)

bot_token = get_token()

client.run(bot_token)

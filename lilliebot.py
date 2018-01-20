import discord
import asyncio
import requests
import io
import os
from lb_pokemon import forms, mega, generate_dict, generate_list
from lb_functions import types, dual_types, mono, ability, nature
from lb_moves import move_info, move_print
from lb_utilities import get_token, stats_print, types_print, mega_print, ability_print, help, nature_print
from lb_typeing import Type, generate_type_table


client = discord.Client()

#Dictionary that contains the Weaknesses, Resistances, Immunities for each type
type_table = generate_type_table()

#Dictionary that contains the csv info with the pokemons name as the key
pokedex = generate_dict()

#List that contains the names of the base pokemon
numbers = generate_list()

#For use with any command that needs to handle multi word names
def args_check(args):
    #arguments will be less than 2 if no args are given
    if len(args) < 2:
        return -1
    #arguments equal to 3 means that the passed arg has a two word name
    elif len(args) == 3:
        #combine the 2 words to make 1 string
        temp = args[1] + ' ' + args[2]
        args[1] = temp
        return args
    # Single word arg is given
    else:
        return args

# Function that downloads the passed link
# Writes it to a temp png and posts it
# Then deletes the temp png
async def pic_print(message, link):
    #Download Image to temp and Post
    r = requests.get(link, stream=True)
    img = io.BytesIO(r.content)

    temporarylocation="pokemon.png"
    with open(temporarylocation,'wb') as out: ## Open temporary file as bytes
        out.write(img.read())                ## Read bytes into file

    await client.send_file(message.channel, temporarylocation)
    os.remove(temporarylocation) ## Delete file when done

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

    # Help
    elif message.content.startswith('*help'):
        await client.send_message(message.channel, help())

    # Pic
    elif message.content.startswith('*pic'):
        args = message.content.upper().split()

        args = args_check(args)

        # No args are passed notify the user
        if args == -1:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            #check to see if a number is passed
            temp = args[1][0:-1]
            if args[1].isnumeric():
                try:
                    info = pokedex[numbers[int(args[1])-1]]
                except Exception as e:
                    info = -1
            elif temp.isnumeric():
                info = forms(args[1])
            else:
                try:
                    info = pokedex[args[1]]
                except Exception as e:
                    info = -1

        if info != -1:
            await pic_print(message, info[0])

    # Stats
    elif message.content.startswith('*stats'):
        args = message.content.upper().split()

        args = args_check(args)

        if args == -1:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            #check to see if a number is passed
            temp = args[1][0:-1]
            if args[1].isnumeric():
                try:
                    info = pokedex[numbers[int(args[1])-1]]
                except Exception as e:
                    info = -1
            elif temp.isnumeric():
                info = forms(args[1])
            else:
                try:
                    info = pokedex[args[1]]
                except Exception as e:
                    info = -1

        if info != -1:
            m = stats_print(info, type_table)

            await pic_print(message, info[0])
            await client.send_message(message.channel, m)

    # Mega
    elif message.content.startswith('*mega'):
        args = message.content.upper().split()

        args = args_check(args)

        if args == -1:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            temp = args[1][0:-1]
            if args[1].isnumeric():
                info = mega(1, args[1])
            elif temp.isnumeric():
                info = mega(1, args[1])
            else:
                info = mega(2, args[1])

        if info != -1:
            m = mega_print(info, type_table)

            await pic_print(message, info[0])
            await client.send_message(message.channel, m)

    # Move
    elif message.content.startswith('*move'):
        args = message.content.upper().split()

        args = args_check(args)

        if args == -1:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            info = move_info(args[1])

            if info != -1:
                m = move_print(info)
                await client.send_message(message.channel, m)

    # Type
    elif message.content.startswith('*type'):
        args = message.content.upper().split()

        # 2 args means search for Mono type pokemon
        if len(args) == 2:
            type_list = mono(args[1])
            if len(type_list) != 0:
                await client.send_message(message.channel, types_print(type_list))
        elif len(args) == 3:
            # The all token was passed so search for all pokemon with the passed type
            if args[1] == "ALL":
                type_list = types(args[2])
                if len(type_list) != 0:
                    await client.send_message(message.channel, types_print(type_list))
            # Two types were passed search for dual type pokemon
            else:
                type_list = dual_types(args[1], args[2])
                if len(type_list) != 0:
                    await client.send_message(message.channel, types_print(type_list))
        else:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')

    # Ability
    elif message.content.startswith('*ability'):
        args = message.content.upper().split()

        args = args_check(args)

        if args == -1:
            await client.send_message(message.channel, '```Invalid arguments type *help for commands```')
        else:
            info = ability(args[1])

            if info != -1:
                m = ability_print(info)
                await client.send_message(message.channel, m)

    # Nature
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

import discord
from discord.ext import commands
import random
import asyncio
import datetime
from random import randint

client = discord.Client()




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------------')
    now_playing = discord.Game(name='>help')
    await client.change_status(game=now_playing, idle=False)
    

#insert logging.txt here to restore logging functions


#Commands and functions 
@client.event
async def on_message(message):

    '''
    Example messasge:

    elif message.content.startswith('>example'):
     msg = await client.send_message(message.channel, 'example')
    '''

    if message.content.startswith('>test'):
      msg = await client.send_message(message.channel, 'hello world')

    elif message.content.startswith('i like bepis bot better'):
        msg = await client.send_message(message.channel, 'i do too')


    elif message.content.startswith('>help'):
        member = message.author
        with open('help.txt', 'r') as help:
         msg = await client.send_message(member, help.read())
         
    elif message.content.startswith('>checkem'):
        msg = await client.send_message(message.channel, random_with_N_digits(2)) 
    
    elif message.content.startswith('>dev'):
        member = message.author
        with open('details.txt', 'r') as develop:
         msg = await client.send_message(member, develop.read())

#Token
client.run('token_insert_here')
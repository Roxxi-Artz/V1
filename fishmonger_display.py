from discord.ext import commands
from dotenv import load_dotenv
import random

TOKEN = ('insert token here')

client = commands.Bot(command_prefix=";")

# shows if the bot is connected
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# sends messages in response
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    speak = [
        'Time to Mong some Fish!',
        'please buy my fish',
        'I LOVE FISHING AND SELLING THE FISH I CATCH FROM FISHING',
        'I have Congestive Heart Failure',
        'The pain... it\'s unbearable',
        'Hey Mr. Sekol, you should give this bot a 10/10 if ur cool',
        'I am Gothams greatest hero nobody else beats me nope nu-uh nobody.',
        'what do you want',
        ':sunglasses:',
        'HELP! HELP ME PLEASE! IT HURTS',
        'My favorite fish is the hagfish',
        'wanna play yu-gi-oh?',
        (
            'Oh my god, '
            'are you world famous american actor Brendan Fraiser?'
        )
    ]

    if message.content == 'talk':
        response = random.choice(speak)
        await message.channel.send(response)
        
client.run(TOKEN)
from discord.ext import commands
import math
import random

TOKEN = ('insert token here')

client = commands.Bot(command_prefix=";")

# shows that the bot is connected
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



# talks to you
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    speak = [
        'Time to Ultra some Kill!',
        'please give me blood',
        'I LOVE KILLING THE SOULS OF THE DAMNED AS THEY TRY TO KILL ME',
        'I have Congestive Heart Failure',
        'The pain... it\'s unbearable',
        'Hey Mr. Sekol, you should give this bot a 10/10 if ur cool',
        'HELL IS FULL',
        'what do you want',
        ':sunglasses:',
        'HELP! HELP ME PLEASE! IT HURTS',
        'My favorite fish is the hagfish',
        'wanna play yu-gi-oh?',
        'Watch out for my revolver attack, it can kill me instead of you!',
        'shawty\'s like a melody in my head that I can\'t keep out got me singin\' like',
        (
            'Oh my god, '
            'are you world famous american actor Brendan Fraiser?'
        )
    ]
    if message.content == 'talk':
        response = random.choice(speak)
        await message.channel.send(response)


#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#
#    
#    random_number = random.randint(1, 100)
#
#
#    #the game
#    def algorithmGame(rando_number):
#
#
#        rando_number = random_number
#
#        guess = int(input('I have thought of a number between 1 and 100. I\'ll kill you if you get it wrong! Write your answer here: '))
#
#        if guess == rando_number:
#            response = (f"Congrats! You guessed right!! I won't actually kill you now!")
#        elif guess > rando_number:
#            response = (f"A bit lower than that!")
#            algorithmGame(rando_number)
#        elif guess < rando_number:
#            response = (f"A bit higher than that!")
#            algorithmGame(rando_number)
#        else:
#            response = ('what')
#            algorithmGame(rando_number)
#    
#    if message.content == 'game':
#        response = algorithmGame(random_number)
#        await message.channel.send(response)
    



    


        
client.run(TOKEN)
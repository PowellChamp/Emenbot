import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Emenbot Ready")

@client.event
async def on_message(message):
    responses = [
        "Shut up retard",
        "Oh my god you are retarded",
        "This opinion is invalid",
        "RIP Horse",
        "Suck your mum",
        "Who asked?",
        "Just leave already",
        "Shut up horse fucker",
        "Go fuck your horse",
        "Shut up Ben",
        "Shut up bitch",
        "David doesn't love you",
        "You're adopted",
        "Fucking dog",
        "You drank sock water...",
        "https://tenor.com/view/mayweather-throwing-ls-gif-7288740"
    ]
    if str(message.author) == "Tom#9518":
        await message.reply(random.choice(responses))

client.run(os.getenv('EMENBOT'))

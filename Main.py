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
        "https://tenor.com/view/mayweather-throwing-ls-gif-7288740",
        "Nonce",
        "Don't care",
        "https://cdn.discordapp.com/attachments/953625837729644584/982343726976364604/unknown.png",
        "https://cdn.discordapp.com/attachments/895043936924618762/982343884875104256/unknown.png",
        "What's your problem with me?\nalways have to be an arsehole don't you"
    ]
    if str(message.author) == "BackRow#1214":
        chance = random.randint(0,5)
        print(chance)
        if chance == 1:
            await message.reply(random.choice(responses))

client.run(os.getenv('EMENBOT'))

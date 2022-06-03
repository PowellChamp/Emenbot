import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Emenbot Ready")

@client.event
async def on_message(message):
    if str(message.author) == "BackRow#1214":
        await message.reply("Shut up retard")

client.run(os.getenv('EMENBOT'))

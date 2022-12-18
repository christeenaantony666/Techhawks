import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    greetings = ["hello"]

    if any(word in message.content.lower()for word in greetings):
        if message.author == client.user:
            return
    
    
    await message.channel.send("Hello there, " + str(message.author))
    print("Reply to hello command has been executed")

client.run(TOKEN)
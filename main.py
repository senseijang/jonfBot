import os
import discord
import random
from stay_alive import stay_alive

# importing quotes from quotes.txt
text_file = open("quotes.txt", "r")
lines = text_file.readlines()
text_file.close()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!random'):
        quoteInt = (random.randrange(len(lines)))
        await message.channel.send(lines[quoteInt])


# logging in the bot into discord.
my_secret = os.environ['token']

stay_alive()
client.run(my_secret)



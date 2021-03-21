from os import getenv
import discord

WORD_COUNT= getenv('WORD_COUNT') or 100
TOKEN = getenv('TOKEN')

client = discord.Client()

windbag = None

@client.event
    async def on_ready(self):
        print('Beep boop I have started')      

@commands.Cog.listener()
async def on_message(self, message):
    if message.author != windbag and len(message.content) > WORD_COUNT:
        await message.channel.send("Sir this is a Wendy's")
        windbag = message.author
        print(f'{message.author} sure is a windbag')
    else if windbag && message.author == windbag:
        await message.channel.send('We serve food here, sir')
        windbag = None
    else:
        windbag = None

bot.run(TOKEN)
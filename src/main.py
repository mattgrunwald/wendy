from os import getenv
from discord.ext import commands
from wendy import Wendy

WORD_COUNT= getenv('WORD_COUNT') or 100
TOKEN = getenv('TOKEN')

client = Wendy(WORD_COUNT)
client.run(TOKEN)
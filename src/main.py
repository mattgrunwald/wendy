from os import getenv
from discord.ext import commands
from wendy import Wendy

WORD_COUNT= getenv('WORD_COUNT') or 100
TOKEN = getenv('TOKEN')

bot = commands.Bot()
bot.add_cog(Wendy(bot, WORD_COUNT))
bot.run(TOKEN)
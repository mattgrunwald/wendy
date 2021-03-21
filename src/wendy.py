class Wendy(commands.Cog):
    def __init__(self, bot, word_count):
        self.bot = bot
        self.windbag = None

    @commands.Cog.listener()
    async def on_ready(self):
        print('Beep boop I have started')
        print(self.member_store)

    @commands.Cog.listener()
    async def on_message(message):
    if len(message.content.split()) > WORD_COUNT:
        await message.channel.send("Sir this is a Wendy's")
        windbag = message.author
        print(f'{message.author} sure is a windbag')
    elif windbag and message.author == windbag:
        await message.channel.send('We serve food here, sir')
        windbag = None
    else:
        windbag = None



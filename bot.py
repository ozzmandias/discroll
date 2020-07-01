import discord
from myconfig import DISCORD_TOKEN
client = discord.Client()

@client.event
async def on_ready():
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return



client.run(DISCORD_TOKEN)

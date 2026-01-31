import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')
    print(f'Bot is in {len(bot.guilds)} servers')

@bot.command()
async def test(ctx):
    await ctx.send('Test command works!')

@bot.command()
async def servers(ctx):
    guild_list = '\n'.join([guild.name for guild in bot.guilds])
    await ctx.send(f'I am in these servers:\n{guild_list}')

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

# Get token from environment variable
bot.run(os.getenv('DISCORD_TOKEN'))
```

**`requirements.txt`** (tells Railway what to install):
```
discord.py==2.3.2
```

**`Procfile`** (tells Railway how to run your bot):
```
worker: python bot.py
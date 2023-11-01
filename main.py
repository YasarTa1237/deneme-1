import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def aga_küfür_etme(ctx):
    await ctx.send("::middle_finger:")

bot.run("MTE2NjgwODI0MzI1MTcyODQ3Ng.GNIURB.q1crbk-xfrGKYO1-53OV-8SmKik_ajkDa4B9zk")


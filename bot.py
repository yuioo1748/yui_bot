import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '【')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

bot.run("ODUyMTIyNjQxMzg4OTI5MDI0.YMCPDQ.HhPTM2MJ-W7vMSSyWTSKEdsfIGE")
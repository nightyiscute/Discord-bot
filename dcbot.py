import discord
from discord.ext import commands
bot=commands.Bot(command_prefix='!')

@bot.event #觸發事件
async def on_ready(): #啟動on_ready函數
    print("bot上線拉")

@bot.event
async def on_member_join(member):
    print(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')

bot.run('OTk5OTg5MDM2MDQxMTIxNzky.GHtIIK.COETGENgHoVZBsnv9QfAAgS6QsRz1RvTpaN30E')
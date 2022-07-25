import discord
from discord.ext import commands
bot=commands.Bot(command_prefix='!')

@bot.event #觸發事件
async def on_ready(): #啟動on_ready函數
    channel=bot.get_channel(999993244425392231)
    await channel.send('機器人上線啦!') #發送訊息
    print("bot上線拉") #在終端發送訊息
@bot.command()
async def ping(ctx): #啟動ping函數
    await ctx.send(f'{round(bot.latency*1000)}'"(ms)")
bot.run('token')


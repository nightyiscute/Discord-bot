import discord
import json
from discord.ext import commands

with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)
bot=commands.Bot(command_prefix='!')

@bot.event #觸發事件
async def on_ready(): #啟動on_ready函數
    channel=bot.get_channel(int(jdata['channel_id']))
    await channel.send('機器人上線啦!') #發送訊息
    print("bot上線拉") #在終端發送訊息
@bot.command()
async def ping(ctx): #啟動ping函數
    await ctx.send(f'{round(bot.latency*1000)}'"(ms)")
bot.run(jdata['token'])


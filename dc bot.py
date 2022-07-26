import imp
import discord
import json
import random
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
    await ctx.send(f'{round(bot.latency*1000)}'"(ms)") #發送延遲毫秒數
    
@bot.command()    
async def photo(ctx): #啟動照片函數(photo是名字)
    random_photo=random.choice (jdata['photo']) #定義ramdom_photo
    photo=discord.File(random_photo) #定義photo=discord的檔案
    await ctx.send (file=photo) #發送檔案

@bot.command()    
async def web_photo(ctx): #啟動照片函數(wed_photo是名字)
    random_photo=random.choice (jdata['url_photo']) #定義ramdom_photo
    await ctx.send(random_photo)

@bot.command()
async def ask(ctx):
    await ctx.send("!ping可偵測延遲 \n!photo可隨機發送圖片 \n!web_photo可以發送網址 \n!ask以查看命令列表")

bot.run(jdata['token'])


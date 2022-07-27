from email import message
import imp
from lib2to3.pgen2 import token
from unicodedata import name
import discord
import json
import random
from pixivpy3 import *
from discord.ext import commands
import os

with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='!')
REFRESH_TOKEN=token
cilent=discord.Client()

@bot.event #觸發事件
async def on_ready(): #啟動on_ready函數
    channel=bot.get_channel(int(jdata['channel_id']))
    await channel.send('機器人上線啦!') #發送訊息
    print("bot上線拉") #在終端發送訊息

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f"cmds.{Filename[:-3]}")


if __name__=="__main__":
    bot.run(jdata['token'])


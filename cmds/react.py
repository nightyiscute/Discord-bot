import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import json
import random

with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

class react(Cog_Extantion):
    @commands.command()    
    async def photo(self,ctx): #啟動照片函數(photo是名字)
        random_photo=random.choice (jdata['photo']) #定義ramdom_photo
        photo=discord.File(random_photo) #定義photo=discord的檔案
        await ctx.send(file=photo) #發送檔案

    @commands.command()    
    async def web_photo(self,ctx): #啟動照片函數(wed_photo是名字)
        random_photo=random.choice (jdata['url_photo']) #定義ramdom_photo
        await ctx.send(random_photo)
async def setup(bot):
    await bot.add_cog(react(bot))
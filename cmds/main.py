import imp
import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import datetime
import random
import json

with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

class Main(Cog_Extantion):
    @commands.command()
    async def ping(self,ctx): #啟動ping函數
        await ctx.send(f'{round(self.bot.latency*1000)}'"(ms)") #發送延遲毫秒數

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @commands.command()
    async def my(self,ctx):
        embed=discord.Embed(title=f"{ctx.author.display_name}", url="https://youtu.be/dQw4w9WgXcQ", description="好康的", color=0x00ff6e,timestamp=datetime.datetime.now())
        embed.set_author(name="Information")
        embed.add_field(name="Never gonna give you up", value="Never gonna run around and desert you", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"{ctx.author.display_name}寫於")
        await ctx.send(embed=embed)

    @commands.command()
    async def luck(self,ctx):
        random_luck=random.choice(jdata["luck"])
        if random_luck=="大吉":
            lcolor=0x00ff1e
            word="恭喜!今天適合買大樂透"
        if random_luck=="吉":
            lcolor=0x00e1ff
            word="恭喜!今天會有小確幸"
        if random_luck=="中":
            lcolor=0xfbff00
            word="今天運氣不好也不壞，是個平常的一天呢"
        if random_luck=="兇":
            lcolor=0xff8800
            word="今天走路要看路喔，小心踩到狗屎"
        if random_luck=="大凶":
            lcolor=0xff0000
            word="小心血光之災!"
        embed=discord.Embed(title=random_luck,  color=lcolor,timestamp=datetime.datetime.now())
        embed.set_author(name="今日運氣")
        embed.add_field(name=word,value="以上就是占卜結果", inline=False)
        embed.set_footer(text=f"{ctx.author.display_name}占卜於")
        await ctx.send(embed=embed)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    
    @commands.command()
    async def dice(self,ctx):
        random_dice=random.choice(jdata["dice"])
        await ctx.send(random_dice)
    
    @commands.command()
    async def time(self,ctx):
        await ctx.send(datetime.datetime.now())

def setup(bot):
    bot.add_cog(Main(bot))


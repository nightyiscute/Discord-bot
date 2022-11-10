import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import datetime
import random
import json
from discord import app_commands

with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

class Main(Cog_Extantion):

    @app_commands.command(name="ping") #ping指令
    async def ping(self,ctx: discord.Interaction): #啟動ping函數
        await ctx.response.send_message(f"{round(self.bot.latency*1000)}(ms)") #發送延遲毫秒數

    @commands.command() #匿名講話指令
    async def say(self,ctx,*,msg):
        await ctx.send(msg)
        await ctx.message.delete()

    @commands.command() #自我介紹指令
    async def my(self,ctx):
        embed=discord.Embed(title=f"{ctx.author.display_name}", url="https://youtu.be/dQw4w9WgXcQ", description="好康的", color=0x00ff6e,timestamp=datetime.datetime.now())
        embed.set_author(name="Information")
        embed.add_field(name="Never gonna give you up", value="Never gonna run around and desert you", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"{ctx.author.display_name}寫於")
        await ctx.send(embed=embed)

    @commands.command() #運氣指令
    async def luck(self,ctx):
        random_int=random.randint(0,100)
        if random_int<10:
            random_luck="大凶"
        if 10<=random_int<30:
            random_luck="兇"
        if 30<=random_int<70:
            random_luck="中"
        if 70<random_int<90:
            random_luck="吉"
        if 90<random_int:
            random_luck="大吉"

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

    @commands.command() #防刷屏指令
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    
    @commands.command() #骰子指令
    async def dice(self,ctx,msg:int):
        random_dice=random.randint(0,msg)
        await ctx.send(random_dice)
    
    @commands.command() #時間指令
    async def time(self,ctx):
        await ctx.send(f"現在是{datetime.datetime.now().strftime('%Y 年 %m 月 %d 日 %H 時 %M 分')}")

    @commands.command() #n網指令
    async def n(self,ctx,msg):
        await ctx.send(f'https://nhentai.net/g/{msg}/')

    @commands.command() #禁漫指令
    async def 禁漫(self,ctx,msg):
        await ctx.send(f'https://18comic.vip/photo/{msg}')
    
    @commands.command()
    async def fuck(self,ctx):
        await ctx.send(f"{ctx.author.display_name}你連一個discord bot都想幹?")


async def setup(bot: commands.Bot): #匯入Cog
    await bot.add_cog(Main(bot))

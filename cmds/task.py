import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import json,asyncio,datetime
import random

class task(Cog_Extantion):
    with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
        jdata=json.load(jfile)
    random.saying=random.choice(jdata["goodmorning"])
    def __init__(self,*args,**kwargs): #格式化class time
        super().__init__(*args,**kwargs) #把classes 的class引用回來
        self.counter=0
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(999993244425392231)
            while not self.bot.is_closed():
                now_time=datetime.datetime.now().strftime("%H%M")
                with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
                    jdata=json.load(jfile)
                if now_time=="0700" and self.counter<1:
                    await self.channel.send(random.saying)
                if now_time=="0701":
                    self.counter=0
                if now_time==jdata['time'] and self.counter<1:
                    await self.channel.send('working!')
                    self.counter=1
                    await asyncio.sleep(3) #單位為秒
                else:
                    await asyncio.sleep(1) #單位為秒
                    pass    

               
                
        self.bg_task=self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel=self.bot.get_channel(ch)
        await ctx.send(f'設定頻道{self.channel.mention}')
    
    @commands.command()
    async def set_time(self,ctx,time):
        self.counter=0
        with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
            jdata=json.load(jfile)
        jdata["time"]=time
        with open('setting.json',mode='w',encoding='utf8')as jfile: #打開setting.json,模式是write,命名為jfile
            json.dump(jdata,jfile,indent=4) #indent是縮排



def setup(bot):   
    bot.add_cog(task(bot))      

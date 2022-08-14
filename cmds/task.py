import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import json,asyncio,datetime


class task(Cog_Extantion):
    def __init__(self,*args,**kwargs): #格式化class time
        super().__init__(*args,**kwargs) #把classes 的class引用回來

        async def interval():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(999993244425392231)
            while not self.bot.is_closed():
                await self.channel.send("owo")
                await asyncio.sleep(5) #單位為秒
        self.bg_task=self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel=self.bot.get_channel(ch)
        await ctx.send(f'設定頻道{self.channel.mention}')




def setup(bot):   
    bot.add_cog(task(bot))      

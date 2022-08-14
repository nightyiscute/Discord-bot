import imp
import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import json,asyncio,datetime


class time(Cog_Extantion):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        async def interval():
            await self.bot.wait_until_ready()
            




def setup(bot):   
    bot.add_cog(time(bot))      

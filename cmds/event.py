import discord
from discord.ext import commands
from core.classes import Cog_Extantion
import random 
import json

with open('setting.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)

class event(Cog_Extantion):
    @commands.Cog.listener()
    async def on_message(self,msg):       
        if msg.author==self.bot.user:
            return        
        if msg.content=="hi":
            random_talk=random.choice(jdata['talk'])
            await msg.channel.send(random_talk)
        if self.bot.user in msg.mentions:
            await msg.channel.send(f"tag三小{msg.author.display_name}")
        
def setup(bot):
    bot.add_cog(event(bot))